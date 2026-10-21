#!/usr/bin/env python3

"""Exercise 4: Most Populated Countries.

Read the countries_data.json file and create a function that creates
a list of the ten most populated countries.
"""

import json


def most_populated_countries(file_path, number):
    """Return a list of the most populated countries.

    Args:
        file_path: Path to the JSON file with countries data.
        number: Number of countries to return.

    Returns:
        A list of dictionaries containing country names and populations.

    Raises:
        ValueError: If number is negative.
    """
    if number < 0:
        raise ValueError("Number must be non-negative.")

    with open(file_path, "r") as file:
        data = json.load(file)

    def get_population(country):
        """Return the population of a country.

        Args:
            country: A dictionary containing country data.

        Returns:
            The population of the country.
        """
        return country["population"]

    sorted_countries = sorted(
        data,
        key=get_population,
        reverse=True,
    )

    top_n_populated_countries = sorted_countries[:number]

    result = []

    for country in top_n_populated_countries:
        result.append(
            {
                "country": country["name"],
                "population": country["population"],
            }
        )

    return result


result = most_populated_countries("countries_data.json", 10)

for country in result:
    print(country)

zero_result = most_populated_countries("countries_data.json", 0)
print("Zero countries:", zero_result)

try:
    most_populated_countries("countries_data.json", -1)
except ValueError as error:
    print(error)

one_result = most_populated_countries("countries_data.json", 1)
print("One country:", one_result)
