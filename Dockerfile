FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./qa /app/qa

RUN PYTHONPATH=. python3 qa/setup.py

ENV PORT=${PORT:-8080}

EXPOSE $PORT
ENTRYPOINT uvicorn qa:app --port $PORT --host 0.0.0.0
# CMD ["--host", "0.0.0.0"]