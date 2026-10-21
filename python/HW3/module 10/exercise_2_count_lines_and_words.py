#!/usr/bin/env python3

"""Exercise 2: Count Lines and Words.

Create a function that counts the number of lines and words in a text file.

Read the Steve Jobs speech file and display the number of lines and words
in the text.
"""


def count_lines_and_words(file_path):
    """Count the number of lines and words in a text file.

    Args:
        file_path: Path to the text file.

    Returns:
        A tuple containing the number of lines and words.
    """
    try:
        with open(file_path, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found!")
        return 0, 0

    lines = text.splitlines()
    line_count = len(lines)

    words = text.split()
    word_count = len(words)

    return line_count, word_count


result = count_lines_and_words("steve_jobs_speech.txt")
print("Number of lines:", result[0])
print("Number of words:", result[1])

count_lines_and_words("potato.txt")

empty_result = count_lines_and_words("empty.txt")
print("Empty file lines:", empty_result[0])
print("Empty file words:", empty_result[1])
