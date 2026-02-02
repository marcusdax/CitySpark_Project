"""
Simple API server for demonstration
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="CitySpark Demo")


@app.get("/")
def root():
    return {"status": "ok", "message": "CitySpark API is running", "version": "demo"}


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "message": "CitySpark Demo Server",
        "timestamp": "2024-01-19T10:45:00",
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
