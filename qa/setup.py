"""
Simple script to preload the pipeline weights in the docker image build
"""
from qa.qa_model import build_pipeline

if __name__ == "__main__":
    build_pipeline()