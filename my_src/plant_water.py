import sys
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch



def getWaterConditions(filename):
    """
    Get the most favorable water scheduling for a species of plant.

    :param filename: the file containing a length of text about the 
        species of plant at large
    :type filename: class 'str'

    :return: a tuple of the plant species and a list containing the answer 
        to the hardcoded question of watering conditions
    :rtype: tuple, first element a string, second element is a list
    """
    tokenizer = AutoTokenizer.from_pretrained(
        "bert-large-uncased-whole-word-masking-finetuned-squad")
    model = AutoModelForQuestionAnswering.from_pretrained(
        "bert-large-uncased-whole-word-masking-finetuned-squad")

    file = open(filename, "r")
    text = file.read()

    questions = [
        "How should we water this plant?"
    ]
    answers = []
    for question in questions:
        inputs = tokenizer.encode_plus(
            question, text, add_special_tokens=True, return_tensors="pt")
        input_ids = inputs["input_ids"].tolist()[0]

        answer_start_scores, answer_end_scores = model(**inputs)

        # Get the most likely beginning of answer with the argmax of the score
        answer_start = torch.argmax(answer_start_scores)
        # Get the most likely end of answer with the argmax of the score
        answer_end = torch.argmax(answer_end_scores) + 1

        answer = tokenizer.convert_tokens_to_string(
            tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end])
        )
        answers.append(answer)
        print(f"Question: {question}")
        print(f"Answer: {answer}\n")
    plantname = filename.rpartition('/')[2][:-4]
    return plantname, answers


if __name__ == "__main__":

    file1 = sys.argv[1]
    getWaterConditions(file1)
