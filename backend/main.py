from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="CrowdSense IIT Jodhpur API",
    description="Real-time Campus Crowd Sensing, Predictive Visit Forecasting & Accessible Wayfinding API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CrowdSense-IITJ-Backend",
        "campus": "IIT Jodhpur (NH 62, Karwar)",
        "timestamp": datetime.utcnow().isoformat()
    }
