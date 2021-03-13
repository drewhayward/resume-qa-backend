from transformers import AutoTokenizer, T5ForConditionalGeneration

model_name = "allenai/unifiedqa-t5-small"


def build_pipeline():

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    def predict(input_string, context):
        input_ids = tokenizer.encode(f"{input_string}\n{context}", return_tensors="pt")
        output = model.generate(input_ids)
        return tokenizer.batch_decode(output, skip_special_tokens=True)[0]

    return predict


if __name__ == "__main__":
    pipeline = build_pipeline()

    print(
        pipeline(
            "Where did you go to school?",
            "I attended Michigan State University for my masters in computer science.",
        )
    )

