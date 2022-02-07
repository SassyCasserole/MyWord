import string
import random


def generate_words():
    words = []
    for i in range(0, 1000):
        words.append(''.join(random.choices(string.ascii_lowercase, k=5)))
    return words
