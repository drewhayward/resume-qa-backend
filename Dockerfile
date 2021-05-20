# FROM huggingface/transformers-pytorch-cpu
FROM python:3.8

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./qa /app/qa

CMD ["uvicorn", "qa.main:app", "--host", "0.0.0.0", "--port", "8080"]