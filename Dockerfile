# FROM huggingface/transformers-pytorch-cpu
# FROM python:3.8
# TODO: Try pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime
FROM pytorch/pytorch

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./qa /app/qa

RUN PYTHONPATH=. python3 qa/setup.py

CMD ["uvicorn", "qa:app", "--host", "0.0.0.0", "--port", "80"]