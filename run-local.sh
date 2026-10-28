#!/bin/bash

# OpsGuardian - Local Fast Runner (No Docker required)
# Traps Ctrl+C to stop all child processes cleanly
trap 'echo "\n🛑 Stopping OpsGuardian..."; kill $(jobs -p) 2>/dev/null; exit' SIGINT SIGTERM EXIT

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

echo "🛡️ Starting OpsGuardian Locally (No Docker mode)..."
echo "================================================="

# 1. Setup Python Virtual Environment if not present
if [ ! -d ".venv" ]; then
    echo "📦 Creating unified local virtual environment (.venv)..."
    python3 -m venv .venv
    source .venv/bin/activate
    echo "⬇️ Installing Python dependencies..."
    pip install --upgrade pip
    pip install -r backend/requirements.txt
    pip install -r ai-engine/requirements.txt
else
    source .venv/bin/activate
fi

# 2. Check if .env exists
if [ ! -f .env ]; then
    cp .env.example .env
fi

# 3. Start AI Engine (Port 8001)
echo "🧠 Starting AI Engine on http://localhost:8001..."
cd "$ROOT_DIR/ai-engine"
python main.py &
AI_PID=$!

# Wait 2 seconds for AI Engine to bind
sleep 2

# 4. Start FastAPI Backend (Port 8000)
echo "🔧 Starting Backend API on http://localhost:8000..."
cd "$ROOT_DIR/backend"
python main.py &
BACKEND_PID=$!

# Wait 2 seconds for Backend to bind
sleep 2

# 5. Start React Frontend (Port 3000)
echo "🌐 Starting React Dashboard on http://localhost:3000..."
cd "$ROOT_DIR/frontend"
npm start


