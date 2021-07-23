from qa.main import build_pipeline


if __name__ == "__main__":
    with open('qa/bio.txt', 'r') as fp:
        bio_text = fp.read()

    with open('questions.txt', 'r') as fp:
        questions = list(fp.readlines())


    pipeline = build_pipeline()
    
    for q in questions:
        answer = pipeline(q, bio_text)
        print('---')
        print(f'Q: {q.strip()}')
        print(f'\tA: {answer}')