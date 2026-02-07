import random

oracle_response = [
    "Yes. The currents of fate align.",
    "No. The threads do not weave in your favor.",
    "Uncertain. Even the stars hesitate.",
    "Patience. Truth ripens slowly.",
    "The answer exists, but you are not yet ready to hear it."
]

def generate_answer(question):
    res = random.choice(oracle_response)
    return res

