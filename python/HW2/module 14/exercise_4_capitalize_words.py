#!/usr/bin/env python3

"""
Exercise 4: Capitalize Words (optional)

Capitalize the first letter of each word in the sentence
"hello world, how are you?" using the functional approach.
"""


def capitalize_word(word):
    """Capitalize the first letter of a word."""
    return word.capitalize()


def capitalize_sentence(sentence):
    """Return a sentence with the first letter of each word capitalized."""
    return " ".join(map(capitalize_word, sentence.split()))


sentence = "hello world, how are you?"

print(capitalize_sentence(sentence))