from fastapi import APIRouter
from data_models.Scoring import ScoringDataInput, ScoringDataResponse
from global_store import projects_store
from sklearn.metrics import accuracy_score

scoring_router = APIRouter()


@scoring_router.post("/ScoreProject", response_model=ScoringDataResponse, tags=['Scoring'])
def score_project(score_data: ScoringDataInput):
    project = projects_store[score_data.project_name]
    models = project.all_models

    scores = []
    for model in models:
        model_accuracy = accuracy_score(
                model.predict(score_data.samples),
                score_data.targets
        )

        scores.append({
            "model": "{}-{}".format(project.project_name, str(model)),
            "accuracy_score": model_accuracy
        })

    score_list = [x["accuracy_score"] for x in scores]
    best_score_index = score_list.index(max(score_list))

    best_model = scores[best_score_index]

    projects_store[score_data.project_name].champion_model = models[best_score_index]

    return ScoringDataResponse(
            project_name=project.project_name,
            scores=scores,
            message="Scoring complete champion Model is {model}".format(model=best_model["model"])
    )
