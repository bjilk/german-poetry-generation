from transformers import pipeline, AutoTokenizer
import sys
import random

tokenizer = AutoTokenizer.from_pretrained('benjamin/gerpt2')
poem_gen = pipeline('text-generation', model='models/gerpt2-dlk', tokenizer=tokenizer)

def generate(seed):
    max_length = random.randint(50, 250)
    generated = poem_gen(seed, max_length=max_length)[0]['generated_text']
    return generated

while True:

    seed = input('Anfang des Gedichts:\t')

    poem = generate(seed)

    print(poem)
    print()

