from fastapi import FastAPI
from pydantic import BaseModel
from engine_bql import BQLHybridEngine

app = FastAPI()

engine = BQLHybridEngine()

class CommandRequest(BaseModel):
    commands: list

@app.post("/api/run")
def run_commands(request: CommandRequest):
    output = engine.run_script(request.commands)
    return {"output": output}

@app.get("/api/ping")
def ping():
    return {"status": "BQL API Running"}
