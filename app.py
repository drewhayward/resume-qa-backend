from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from qa_model import build_pipeline, get_bio

app = FastAPI()

nlp_pipeline = build_pipeline()
bio_txt = get_bio()


class QuestionRequest(BaseModel):
    question: str


origins = [
    "http://localhost:3000",
    "https://drewhayward.dev",
    "https://drewhayward.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/question/")
def answer_question(q: QuestionRequest):
    answer = nlp_pipeline(q, bio_txt)
    return {"answer": answer}
