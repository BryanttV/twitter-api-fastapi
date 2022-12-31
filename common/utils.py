"""Common helpers module"""
import json


def create_mock(route: str, data: dict) -> None:
    """Creates a mock record.

    Args:
        route (str): route of the mock
        data (dict): data of the mock
    """
    with open(route, "r+", encoding="utf-8") as file:

        results: list = json.load(file)

        results.append(data)

        file.seek(0)

        json.dump(results, file)
