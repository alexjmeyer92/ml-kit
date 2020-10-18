from typing import List, Any
from pydantic import BaseModel


class PredictInput(BaseModel):
    project_name: str
    input_data: List[List[Any]]


class PredictResponse(BaseModel):
    project_name: str
    model_type: str
    predictions: List[Any]
    inputs: List[Any]
