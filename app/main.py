from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="CognitiveFlow Engine")

class ProcessStep(BaseModel):
    name: str
    duration_minutes: int
    manual: bool

class ProcessInput(BaseModel):
    process_name: str
    steps: List[ProcessStep]

@app.post("/analyze")
def analyze_process(process: ProcessInput):
    bottlenecks = []
    automation_candidates = []

    for step in process.steps:
        if step.duration_minutes > 30:
            bottlenecks.append(step.name)
        if step.manual:
            automation_candidates.append(step.name)

    return {
        "process": process.process_name,
        "bottlenecks": bottlenecks,
        "automation_suggestions": automation_candidates,
        "summary": "Process analyzed successfully"
    }

