from typing import List, Any, Dict
from pydantic import BaseModel


class ScoringDataInput(BaseModel):
    project_name: str
    samples: List[List[Any]]
    targets: List[Any]

class ScoringDataResponse(BaseModel):
    project_name: str
    scores: List[Dict[str,Any]]
    message: str
