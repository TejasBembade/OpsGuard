"""Authentication routes"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta
import os

router = APIRouter()
SECRET_KEY = os.getenv("JWT_SECRET", "opsguardian-secret-key")
ALGORITHM = "HS256"

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(req: LoginRequest):
    """Simple admin login - extend for production use"""
    if req.username == "admin" and req.password in ["opsguardian123", "autohealops123"]:
        payload = {"sub": req.username, "exp": datetime.utcnow() + timedelta(hours=24)}
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
