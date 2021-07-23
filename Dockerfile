FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./qa /app/qa

RUN PYTHONPATH=. python3 qa/setup.py

ENTRYPOINT ["uvicorn", "qa:app"]
CMD ["--host", "0.0.0.0", "--port", "80"]