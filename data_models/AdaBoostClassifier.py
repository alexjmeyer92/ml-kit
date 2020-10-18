from pydantic import BaseModel
from typing import Any, List


class AdaBoostClassifierTrainingInput(BaseModel):
    targets: List[Any]
    samples: List[List[Any]]
    project_name: str
