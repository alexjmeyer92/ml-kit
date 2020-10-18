FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./main.py /app
COPY ./global_store.py /app
COPY ./requirements.txt /app
COPY ./data_models/* /app/data_models/
COPY ./routes/* /app/routes/

RUN pip install scikit-learn
