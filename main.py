from fastapi import FastAPI
from data_models.PredictionModels import PredictInput, PredictResponse
from data_models.Project import ProjectModel
from global_store import projects_store
from routes.Classifiers import classifier_router
from routes.Scoring import scoring_router

app = FastAPI()


@app.get("/", tags=['Core'])
async def root():
    return "This is the ml-kit API"


@app.post("/CreateProject", tags=['Core'])
async def create_new_project(project_name: str):
    projects_store[project_name] = ProjectModel(
            project_name=project_name,
            champion_model=None,
            all_models=[]
    )

    return "project {} created successfully".format(project_name)


@app.get("/ListProjects", tags=['Core'])
async def list_projects():
    return list(projects_store.keys())


@app.get("/GetProjectDetails", response_model=ProjectModel, tags=['Core'])
async def get_project_details(project_name: str):
    project = projects_store[project_name]
    return ProjectModel(
            project_name=project.project_name,
            champion_model=str(project.champion_model),
            all_models=[str(x) for x in project.all_models]
    )


@app.get("/PredictProject", response_model=PredictResponse, tags=['Core'])
def predict_project(input_data: PredictInput):
    project = projects_store[input_data.project_name]
    model = project.champion_model
    predictions = model.predict(input_data.input_data)

    return PredictResponse(
            project_name=input_data.project_name,
            model_type=str(model),
            predictions=predictions.tolist(),
            inputs=input_data.input_data
    )


app.include_router(classifier_router)
app.include_router(scoring_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app)
