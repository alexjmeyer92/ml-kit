# ml-kit
Project to play with creating a basic ML As A Service API

## Core Dependencies
sklearn
fastapi
uvicorn

## Docker
https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
docker build -t mlkit .
docker run -i -p 8000:80 mlkit:latest

docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname