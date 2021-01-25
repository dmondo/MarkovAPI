"""Markov model tests."""
from unittest import TestCase

from src.helpers import markov


def test_build_model() -> None:
    """It constructs a dictionary representing a markov model from text."""
    test_data = ["This is some is some sample text"]
    model = markov.build_model(test_data, 2)
    expected_model = {
        "This is": ["some"],
        "is some": ["is", "sample"],
        "some is": ["some"],
        "some sample": ["text"],
    }
    TestCase().assertDictEqual(model, expected_model)


def test_model_removes_links() -> None:
    """Build_model removes http link from text before building."""
    test_data = ["This is some is some sample text https://fake_url.com"]
    model = markov.build_model(test_data, 2)
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
    model = markov.build_model(test_data, 2)
    chain = markov.generate_chain(model=model, length=3, order=2)
    assert len(chain.split(" ")) >= 2

    test_data = ["blah blah blah blah"]
    model = markov.build_model(test_data, 1)
    chain = markov.generate_chain(model=model, length=5, order=1)
    assert chain == "blah blah blah blah blah"

    test_data = ["no possibilities"]
    model = markov.build_model(test_data, 1)
    chain = markov.generate_chain(model=model, length=3, order=1)
    assert len(chain.split(" ")) <= 2


def test_generate_chains() -> None:
    """It generates chains up to the retry limit by calling generate_chain."""
    test_data = ["This is some is some sample text"]
    model = markov.build_model(test_data, 2)
    num_chains = 5
    chains = markov.generate_chains(
        model=model, length=2, order=2, num_chains=num_chains
    )
    assert len(chains) == num_chains

    test_data = ["This chain will never reach the desired length"]
    model = markov.build_model(test_data, 2)
    num_chains = 1
    chains = markov.generate_chains(
        model=model, length=15, order=2, num_chains=num_chains
    )
    assert len(chains) == num_chains
