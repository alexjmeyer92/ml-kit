from pydantic import BaseModel
from typing import Any, List

class TrainingResponse(BaseModel):
    project_name: str
    message: str