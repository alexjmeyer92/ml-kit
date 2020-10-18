from data_models.RFClassifier import RFClassifierTrainingInput
from data_models.AdaBoostClassifier import AdaBoostClassifierTrainingInput
from data_models.TrainingModels import TrainingResponse
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from fastapi import APIRouter
from global_store import projects_store

classifier_router = APIRouter()


@classifier_router.post("/TrainRFClassifier", response_model=TrainingResponse, tags=['Training', 'Classifiers'])
def train_rf_classifier(train_data: RFClassifierTrainingInput):
    samples = train_data.samples
    targets = train_data.targets

    classifier = RandomForestClassifier(random_state=0)

    classifier.fit(X=samples, y=targets)

    projects_store[train_data.project_name].all_models.append(classifier)

    return TrainingResponse(
            project_name=train_data.project_name,
            message="trained successfully"
    )


@classifier_router.post("/TrainAdaBoostClassifier", response_model=TrainingResponse, tags=['Training', 'Classifiers'])
def train_rf_classifier(train_data: AdaBoostClassifierTrainingInput):
    samples = train_data.samples
    targets = train_data.targets

    classifier = AdaBoostClassifier(n_estimators=100)

    classifier.fit(X=samples, y=targets)

    projects_store[train_data.project_name].all_models.append(classifier)

    return TrainingResponse(
            project_name=train_data.project_name,
            message="trained successfully"
    )
