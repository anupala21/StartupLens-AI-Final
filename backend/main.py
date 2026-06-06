from fastapi import FastAPI
from pydantic import BaseModel

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