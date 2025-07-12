from typing import List
from fastapi import APIRouter, HTTPException
from src.schemas import InputsUser, OutputsUser, InputsEvaluator, ChatRequest
from src.agent import agent_advisor, prompt_advisor, agent_evaluator, prompt_evaluator
from src.tools import query_data

router = APIRouter()


# Keep direct evaluator endpoint for testing
@router.post("/evaluator", response_model=OutputsUser)
async def evaluate_credit(inputs: InputsEvaluator):
    """
    Direct endpoint to evaluate credit based on complete user inputs.
    """
    try:
        prompt = prompt_evaluator(inputs)
        response = agent_evaluator(prompt)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))