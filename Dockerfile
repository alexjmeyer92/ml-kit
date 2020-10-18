FROM python:3.8

RUN pip install fastapi uvicorn scikit-learn

EXPOSE 80

COPY ./data_models/* /app/data_models/
COPY ./routes/* /app/routes/
COPY ./main.py /app
COPY ./global_store.py /app

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
#CMD ["python"]