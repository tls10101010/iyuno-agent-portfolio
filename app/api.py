 
from fastapi import FastAPI

app = FastAPI(title="Iyuno Agent Portfolio")


@app.get("/")
def home():
    return {
        "project": "Iyuno Agentic Knowledge Triage",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "ok"}