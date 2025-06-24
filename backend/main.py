from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from engine_bql import BQLHybridEngine

app = FastAPI(title="BQL Hybrid Quantum API", version="2.0.0")
engine = BQLHybridEngine()

class CommandRequest(BaseModel):
    commands: list

@app.post("/run/")
def run_commands(request: CommandRequest):
    try:
        output = engine.run_script(request.commands)
        return {"output": output}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

