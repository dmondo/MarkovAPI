"""Markov model tests."""
from unittest import TestCase

from src.helpers.markov import build_model, generate_chain


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


def test_generate_chain() -> None:
    """It generates a markov chain from a given model."""
    test_data = ["This is some is some sample text"]
    model = build_model(test_data, 2)
    chain = generate_chain(model=model, length=3, order=2)
    assert len(chain.split(" ")) >= 2

    test_data = ["blah blah blah blah"]
    model = build_model(test_data, 1)
    chain = generate_chain(model=model, length=5, order=1)
    assert chain == "blah blah blah blah blah"

    test_data = ["no possibilities"]
    model = build_model(test_data, 1)
    chain = generate_chain(model=model, length=3, order=1)
    assert len(chain.split(" ")) <= 2
