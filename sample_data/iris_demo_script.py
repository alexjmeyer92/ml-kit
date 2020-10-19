import requests
import json

"""
This script will explore using the ML Kit demo API to train, score, and deploy classification models
on the iris data set. This demo service supports Random Forest and AdaBoost Classifiers and helps demonstrate
as a general concept how an API service could be used to simplify the process of training and deploying these types of models
API Swagger Docs Are available here: http://localhost:8000/docs
"""
# Set some constants that will be used later
mlkit_url = "https://alexjmeyer92-mlkit-1428.zeet.app/"

# Fill in your desired project name here.
# I think the only constraint is no spaces in the name
project_name = ""

# Now let's load the iris data set
with open("./sample_data/iris_data.json", "r") as f:
    iris_data = json.load(f)

# The sample iris data is pre split into three groups of data. 1 for training, 1 for scoring, and finally a small sample are held out to
# simulate running predictions once the model is scored and deployed
print(iris_data.keys())

"""
This demo of the ML Kit API will walk through creating a project that will house the models. We will then explore the attributes of that project,
train several models, score the models and determine a champion and finally this champion model will be automatically deployed for running predictions
"""

# Check that the API is running and reachable
api_check = requests.get(mlkit_url)
print("api responded with status {}".format(api_check.status_code))
print("response text: {}".format(api_check.text))

# use the create project endpoint to set up our project
# The project will store our models and should be used to organize work for a single prediction task
create_project = requests.post(
        "{base_url}{path}".format(base_url=mlkit_url, path="CreateProject?project_name={}".format(project_name)))
print("api responded with status {}".format(create_project.status_code))
print("response text: {}".format(create_project.text))

# Check that the service recognizes the project using ListProjects endpoint
list_projects = requests.get("{base_url}{path}".format(base_url=mlkit_url, path="ListProjects"))
print("api responded with status {}".format(list_projects.status_code))
print("response text: {}".format(list_projects.text))

# Look at some details about the project we just created
project_details = requests.get(
        "{base_url}{path}".format(base_url=mlkit_url, path="GetProjectDetails?project_name={}".format(project_name)))
print("api responded with status {}".format(project_details.status_code))
print("response text: {}".format(project_details.text))
# you will see in the response that the project is identifies by its name. It will also have a list that will
# show all of the models that have been trained for the project as well as a champion model.
# The champion model will eventually be used for deployment / prediction and will only populate once
# models have been trained and the project has been scored

# Now let's train both RandomForest & AdaBoost for this project
# We can do this by making post requests to the appropriate endpoint on the API and passing a JSON body containing the
# training data contained at the training key of the iris_data that we loaded earlier
training_samples = iris_data['train']['samples']
training_targets = iris_data['train']['targets']

# Random Forest
# @todo: pick back up here and finish the tutorial / example
rf_training = requests.post(
        url="{base_url}{path}".format(base_url=mlkit_url, path="TrainRFClassifier"),
        json={
            "project_name": project_name,
            "samples": training_samples,
            "targets": training_targets
        }
)
print("api responded with status {}".format(rf_training.status_code))
print("response text: {}".format(rf_training.text))

# Train AdaBoost on our data
adaboost_training = requests.post(
        url="{base_url}{path}".format(base_url=mlkit_url, path="TrainAdaBoostClassifier"),
        json={
            "project_name": project_name,
            "samples": training_samples,
            "targets": training_targets
        }
)
print("api responded with status {}".format(adaboost_training.status_code))
print("response text: {}".format(adaboost_training.text))

# Check back on project details and we can see that both RF and AdaBoost
# Have been trained for our iris predection project
project_details = requests.get(
        "{base_url}{path}".format(base_url=mlkit_url, path="GetProjectDetails?project_name={}".format(project_name)))
print("api responded with status {}".format(project_details.status_code))
print("response text: {}".format(project_details.text))

"""
Now that the project has these two models trained on our data
ml kit can score both models and will automatically deploy the highest
performing one for future predection
"""
scoring_samples = iris_data['score']['samples']
scoring_targets = iris_data['score']['targets']

project_scoring = requests.post(
        url="{base_url}{path}".format(base_url=mlkit_url, path="ScoreProject"),
        json={
            "project_name": project_name,
            "samples": scoring_samples,
            "targets": scoring_targets
        }
)
print("api responded with status {}".format(project_scoring.status_code))
print("response text: {}".format(project_scoring.text))
# In the message from a successful response we can see the champion model for this data set


"""
Now that the project has trained models and has been scored for a champion we can try to predict some records
"""
prediction_inputs = iris_data['predict']['input_samples']
correct_predictions = iris_data['predict']['correct_answers']

project_prediction = requests.get(
        url="{base_url}{path}".format(base_url=mlkit_url, path="PredictProject"),
        json={
            "project_name": project_name,
            "input_data": prediction_inputs
        }
)
print("api responded with status {}".format(project_prediction.status_code))
print("response text: {}".format(project_prediction.text))

# check how well we did
prediction_output = json.loads(project_prediction.text)

predictions = prediction_output['predictions']
print(predictions)
print(correct_predictions)
