from pydantic import BaseModel
from typing import Any, List


class RFClassifierTrainingInput(BaseModel):
    targets: List[Any]
    samples: List[List[Any]]
    project_name: str
