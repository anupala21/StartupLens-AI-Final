from fastapi import FastAPI
from pydantic import BaseModel
from backend.agents.idea_agent import IdeaAgent
from backend.services.gemini_service import GeminiService
app = FastAPI(title="StartupLens AI")


class IdeaRequest(BaseModel):
    idea: str


@app.get("/")
def home():
    return {"message": "StartupLens AI Backend Running"}


@app.post("/validate")
def validate_idea(request: IdeaRequest):

    return {
        "idea": request.idea,
        "status": "received"
    }