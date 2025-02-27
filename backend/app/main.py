from fastapi import FastAPI
from pydantic import BaseModel
from core import ai_feedback
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

@app.post("/analyze")
async def analyze_code(request: CodeRequest):
    code = request.code
    result = ai_feedback.analyze_and_fix_code(code)
    return {"fixed_code": result}

