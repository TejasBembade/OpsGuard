<!-- Animated Header -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0f1d,30:0f172a,60:1e293b,100:070b14&height=250&section=header&text=OpsGuardian%20%F0%9F%9B%A1%EF%B8%8F&fontSize=60&fontColor=38bdf8&fontAlignY=38&desc=Monitor.%20Detect.%20Recover.%20%E2%80%94%20AI-Powered%20Kubernetes%20Self-Healing&descAlignY=58&descSize=18&descFontColor=f1f5f9&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" />
  <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white" />
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Tagline-Monitor.%20Detect.%20Recover.-0ea5e9?style=flat-square" />
</p>

---

## 🛡️ What is OpsGuardian?

> **OpsGuardian** is an enterprise-grade, AI-powered DevOps and SRE platform built on the philosophy: **Monitor. Detect. Recover.** It gives your Kubernetes cluster **the ability to heal itself**. It watches your cluster 24/7, detects anomalies using machine learning, predicts failures before they crash your system, and automatically takes recovery actions — all without human intervention.

```
┌─────────────────────────────────────────────────────────┐
│              OpsGuardian Architecture                   │
├──────────────┬──────────────┬──────────────┬────────────┤
│  Prometheus  │  AI Engine   │  Backend API │  Frontend  │
│  (Metrics)   │  (Anomaly+   │  (FastAPI +  │  (React +  │
│              │  Prediction) │  WebSockets) │  Tailwind) │
├──────────────┴──────────────┴──────────────┴────────────┤
│              Kubernetes Cluster (Minikube/EKS)           │
│  Pods | Deployments | Services | Autoscaler | RBAC       │
└─────────────────────────────────────────────────────────┘
```

---

## ✨ Core Features

<table>
<tr>
<td align="center" width="25%">

### 🔍 AI Fault Detection
Isolation Forest + LSTM anomaly detection on CPU, Memory, Pod restarts & Network latency

</td>
<td align="center" width="25%">

### ⚡ Predictive Failure
LSTM time-series forecasting predicts node/pod failures with probability scores & time-to-failure estimates

</td>
<td align="center" width="25%">

### 🔧 Self-Healing
Automatically restarts pods, reschedules workloads, scales deployments using Kubernetes Python client

</td>
<td align="center" width="25%">

### 📊 Live Dashboard
React + Tailwind UI with WebSocket real-time updates, Chart.js graphs, alerts & AI predictions

</td>
</tr>
</table>

---

## 🏗️ System Architecture

```
                        ┌──────────────────────┐
                        │   React Dashboard     │
                        │  (Port 3000)          │
                        └──────────┬───────────┘
                                   │ WebSocket + REST
                        ┌──────────▼───────────┐
                        │   FastAPI Backend     │
                        │   (Port 8000)         │
                        └──┬───────────────┬───┘
                           │               │
             ┌─────────────▼──┐    ┌───────▼──────────┐
             │  AI Engine      │    │   MongoDB         │
             │  (Port 8001)    │    │   (Port 27017)    │
             │  Isolation      │    │   Metrics + Logs  │
             │  Forest + LSTM  │    └──────────────────┘
             └─────────────────┘
                           │
             ┌─────────────▼──────────────┐
             │     Prometheus              │
             │     (Port 9090)             │
             │     Metrics Scraping        │
             └─────────────┬──────────────┘
                           │
             ┌─────────────▼──────────────┐
             │   Kubernetes Cluster        │
             │   (Minikube / EKS)          │
             │   Pods | Nodes | Services   │
             └────────────────────────────┘
```

---

## 📁 Project Structure

```
OpsGuardian/
│
├── 📂 frontend/                    ← React + Tailwind Dashboard
│   ├── 📂 src/
│   │   ├── 📂 components/          ← Reusable UI components
│   │   ├── 📂 pages/               ← Dashboard, Alerts, Logs pages
│   │   ├── 📂 hooks/               ← Custom React hooks (WebSocket)
│   │   ├── 📂 services/            ← API call services
│   │   └── App.jsx
│   ├── package.json
│   └── tailwind.config.js
│
├── 📂 backend/                     ← FastAPI REST + WebSocket server
│   ├── 📂 controllers/             ← Business logic handlers
│   ├── 📂 routes/                  ← API route definitions
│   ├── 📂 services/                ← DB, Kafka, K8s service connectors
│   ├── main.py
│   └── requirements.txt
│
├── 📂 ai-engine/                   ← ML Models & Training
│   ├── 📂 anomaly_detection/       ← Isolation Forest model
│   ├── 📂 prediction_model/        ← LSTM forecasting model
│   ├── 📂 training/                ← Training scripts
│   ├── main.py
│   └── requirements.txt
│
├── 📂 k8s/                         ← Kubernetes manifests
│   ├── deployments.yaml
│   ├── services.yaml
│   ├── autoscaler.yaml
│   └── rbac.yaml
│
├── 📂 monitoring/                  ← Prometheus + Grafana configs
│   ├── prometheus.yml
│   └── 📂 grafana/
│       └── dashboard.json
│
├── 📂 scripts/                     ← Automation scripts
│   ├── auto-heal.py
│   ├── data-generator.py
│   └── setup.sh
│
├── 📂 docs/                        ← Full documentation
│   ├── SRS.md
│   ├── architecture.md
│   └── setup-guide.md
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Required tools
npm >= 18.x
python >= 3.9
docker >= 24.x
docker-compose >= 2.x
minikube >= 1.30
kubectl >= 1.27
```

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/manikantbindass/AutoHealOps-Self-Healing-Kubernetes-Cluster-with-AI-Fault-Detection.git
cd AutoHealOps-Self-Healing-Kubernetes-Cluster-with-AI-Fault-Detection
```

### 2️⃣ One-Command Setup

```bash
# Make setup script executable
chmod +x scripts/setup.sh

# Run full setup (installs all dependencies)
./scripts/setup.sh
```

### 3️⃣ Manual Setup (Step by Step)

```bash
# Step 1: Copy environment variables
cp .env.example .env

# Step 2: Start all services with Docker Compose
docker-compose up --build

# Step 3: Start Minikube
minikube start --memory=4096 --cpus=2

# Step 4: Apply Kubernetes manifests
kubectl apply -f k8s/

# Step 5: Access dashboard
open http://localhost:3000
```

---

## 🧪 Test Cases

| Scenario | Expected Action | Status |
|----------|----------------|--------|
| Pod crash | Auto restart within 30s | ✅ |
| Memory spike >85% | Scale deployment up | ✅ |
| Node failure | Reschedule pods | ✅ |
| High latency >500ms | Alert + prediction | ✅ |
| CPU >90% | Alert + horizontal scale | ✅ |

---

## 🔐 Security

- **RBAC** — Kubernetes Role-Based Access Control configured
- **JWT Auth** — All API endpoints secured with JWT tokens
- **Secrets** — Kubernetes Secrets for sensitive data
- **TLS** — HTTPS for production deployments

---

## 📈 Roadmap

- [x] Core anomaly detection (Isolation Forest)
- [x] Self-healing scripts
- [x] Prometheus + Grafana monitoring
- [x] React dashboard with WebSockets
- [ ] LSTM predictive model training
- [ ] Reinforcement Learning healing decisions
- [ ] Multi-cluster support
- [ ] Chaos Engineering integration
- [ ] AI Explainability dashboard

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [📋 SRS](./docs/SRS.md) | Software Requirements Specification |
| [🏗️ Architecture](./docs/architecture.md) | Detailed system architecture |
| [🔧 Setup Guide](./docs/setup-guide.md) | Complete installation guide |

---

## 🤝 Contributing

```bash
# Fork → Clone → Branch → Code → PR
git checkout -b feature/your-feature
git commit -m "feat: add your feature"
git push origin feature/your-feature
```

---

<!-- Footer Wave -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:302b63,100:0f0c29&height=120&section=footer" />
</p>

<p align="center">
  <b>⭐ Star this repo if it helped you! Built with ❤️ by <a href="https://github.com/manikantbindass">Manikant Kumar</a></b>
</p>
