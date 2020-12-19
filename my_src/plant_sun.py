from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
import os
os.chdir('my_src/')


def getSunConditions(plantName):
    tokenizer = AutoTokenizer.from_pretrained(
        "bert-large-uncased-whole-word-masking-finetuned-squad")
    model = AutoModelForQuestionAnswering.from_pretrained(
        "bert-large-uncased-whole-word-masking-finetuned-squad")

    file = open("care_files/"+plantName+".txt", "r")
    text = file.read()

    questions = [
        "What type of light does this plant need?",
        "Can you give too much direct light?"
    ]

    for question in questions:
        inputs = tokenizer.encode_plus(
            question, text, add_special_tokens=True, return_tensors="pt")
        input_ids = inputs["input_ids"].tolist()[0]

        text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
        answer_start_scores, answer_end_scores = model(**inputs)

        answer_start = torch.argmax(
            answer_start_scores
        )  # Get the most likely beginning of answer with the argmax of the score
        # Get the most likely end of answer with the argmax of the score
        answer_end = torch.argmax(answer_end_scores) + 1

        answer = tokenizer.convert_tokens_to_string(
            tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

        print(f"Question: {question}")
        print(f"Answer: {answer}\n")


getSunConditions('alocasia')
