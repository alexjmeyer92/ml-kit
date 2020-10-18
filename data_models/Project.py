from typing import List, Any
from pydantic import BaseModel


class ProjectModel(BaseModel):
    project_name: str
    champion_model: Any
    all_models: List[Any]
