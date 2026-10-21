#!/usr/bin/env python3

"""Exercise 3: Most Spoken Languages.

Read the countries_data.json file and create a function that finds the
ten most spoken languages.
"""

import json


def get_count(item):
    """Return the count from a language-count pair.

    Args:
        item: A tuple containing a language and its count.

    Returns:
        The language count.
    """
    return item[1]


def most_spoken_languages(file_path, number):
    """Return the most spoken languages from a countries data file.

    Args:
        file_path: Path to the JSON file with countries data.
        number: Number of languages to return.

    Returns:
        A list of tuples containing language counts and language names.

    Raises:
        ValueError: If number is negative.
    """
    if number < 0:
        raise ValueError("Number must be non-negative.")

    with open(file_path, "r") as file:
        data = json.load(file)

    language_counts = {}

    for country in data:
        for language in country["languages"]:
            if language in language_counts:
                language_counts[language] += 1
            else:
                language_counts[language] = 1

    sorted_languages = sorted(
        language_counts.items(),
        key=get_count,
        reverse=True,
    )

    top_n_languages = sorted_languages[:number]

    result = []

    for item in top_n_languages:
        result.append((item[1], item[0]))

    return result


result = most_spoken_languages("countries_data.json", 10)

for language in result:
    print(language)

zero_result = most_spoken_languages("countries_data.json", 0)
print("Zero languages:", zero_result)

large_result = most_spoken_languages("countries_data.json", 1000)
print("Large number of languages:", len(large_result))

try:
    most_spoken_languages("countries_data.json", -1)
except ValueError as error:
    print(error)
