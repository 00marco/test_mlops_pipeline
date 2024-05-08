# Use the official MLflow Docker image as base image
FROM python:3.9-slim

COPY . .

# Set environment variables
ENV MLFLOW_HOME /mlflow
ENV MLFLOW_TRACKING_URI sqlite:///${MLFLOW_HOME}/mlflow.db

# Install MLflow
RUN pip install -r requirements.txt

# Expose the MLflow UI port
EXPOSE 8889

# Run MLflow UI
CMD mlflow ui --host 0.0.0.0 --port 8889 --backend-store-uri ${MLFLOW_TRACKING_URI}
