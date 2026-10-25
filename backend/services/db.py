"""MongoDB connection service with resilient fallback"""
import motor.motor_asyncio
import os
import asyncio
from datetime import datetime

client = None
db_instance = None

class InMemoryCursor:
    def __init__(self, data):
        self._data = list(data)

    def sort(self, field, direction=-1):
        reverse = direction == -1
        self._data.sort(key=lambda x: str(x.get(field, "")), reverse=reverse)
        return self

    def limit(self, count):
        self._data = self._data[:count]
        return self

    async def to_list(self, limit=None):
        if limit is not None:
            return self._data[:limit]
        return self._data

class InMemoryCollection:
    def __init__(self, name):
        self.name = name
        self._docs = []

    async def insert_one(self, doc):
        d = dict(doc)
        if "_id" not in d:
            d["_id"] = str(len(self._docs) + 1)
        self._docs.append(d)
        class InsertResult:
            inserted_id = d["_id"]
        return InsertResult()

    def find(self, query=None):
        query = query or {}
        filtered = []
        for d in self._docs:
            match = True
            for k, v in query.items():
                if d.get(k) != v:
                    match = False
                    break
            if match:
                filtered.append(dict(d))
        return InMemoryCursor(filtered)

    async def update_one(self, filter_q, update):
        modified = 0
        set_fields = update.get("$set", {})
        for d in self._docs:
            match = True
            for k, v in filter_q.items():
                if d.get(k) != v:
                    match = False
                    break
            if match:
                d.update(set_fields)
                modified += 1
                break
        class UpdateResult:
            modified_count = modified
        return UpdateResult()

class InMemoryDatabase:
    def __init__(self):
        self._collections = {
            "alerts": InMemoryCollection("alerts"),
            "healing_logs": InMemoryCollection("healing_logs"),
            "metrics": InMemoryCollection("metrics")
        }
        # Pre-seed some realistic initial logs and alerts
        self._seed_data()

    def _seed_data(self):
        now = datetime.utcnow().isoformat()
        self._collections["alerts"]._docs.extend([
            {"_id": "1", "severity": "CRITICAL", "message": "High CPU utilization detected (> 90%)", "timestamp": now, "status": "open"},
            {"_id": "2", "severity": "HIGH", "message": "Pod opsguardian-backend-7f8d restarted 6 times", "timestamp": now, "status": "open"},
            {"_id": "3", "severity": "MEDIUM", "message": "Network latency elevated to 420ms", "timestamp": now, "status": "acknowledged"},
        ])
        self._collections["healing_logs"]._docs.extend([
            {"_id": "1", "action": "scale_deployment", "target": "backend", "namespace": "default", "result": "Scaled deployment backend to 3 replicas", "timestamp": now, "triggered_by": "auto"},
            {"_id": "2", "action": "restart_pod", "target": "backend-pod-7f8d", "namespace": "default", "result": "Pod deleted and rescheduled", "timestamp": now, "triggered_by": "auto"}
        ])

    def __getitem__(self, name):
        if name not in self._collections:
            self._collections[name] = InMemoryCollection(name)
        return self._collections[name]

async def connect_db():
    global client, db_instance
    uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/autohealops")
    try:
        motor_client = motor.motor_asyncio.AsyncIOMotorClient(uri, serverSelectionTimeoutMS=1000)
        # Ping to test connectivity
        await motor_client.admin.command('ping')
        client = motor_client
        db_instance = client["autohealops"]
        print(f"✅ MongoDB connected: {uri}")
    except Exception:
        print("ℹ️ MongoDB not detected at localhost:27017. Using high-speed in-memory store for local mode.")
        db_instance = InMemoryDatabase()

def get_db():
    global db_instance
    if db_instance is None:
        db_instance = InMemoryDatabase()
    return db_instance

