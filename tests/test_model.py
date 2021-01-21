"""Markov model tests."""
from unittest import TestCase

from src.helpers.markov import build_model


def test_build_model() -> None:
    """It constructs a dictionary representing a markov model from text."""
    test_data = ["This is some is some sample text"]
    model = build_model(test_data, 2)
    expected_model = {
        "This is": ["some"],
        "is some": ["is", "sample"],
        "some is": ["some"],
        "some sample": ["text"],
    }
    TestCase().assertDictEqual(model, expected_model)
