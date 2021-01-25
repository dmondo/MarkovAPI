"""Helper functions to build Markov model."""

import random
import re
from typing import Dict, List


def build_model(text_data: List[str], order: int) -> Dict[str, List[str]]:
    """Build n-grams markov model of order n from text.

    Args:
        text_data: A list of texts passed to the API.
        order: The order of the n-grams model to build.

    Returns:
        An n-gram markov model of the specified order.
    """
    model: Dict[str, List[str]] = {}

    for corpus in text_data:
        raw_text = re.sub(r"[^A-Za-z0-9 ]+", "", corpus)
        text = re.sub(r"(?:\s)http[^, ]*", "", raw_text).split(" ")

        for i in range(len(text) - order):
            n_gram = " ".join(text[i : i + order])

            if n_gram not in model:
                model[n_gram] = []
            model[n_gram].append(text[i + order])

    return model


def generate_chains(
    model: Dict[str, List[str]], length: int, order: int, num_chains: int
) -> List[str]:
    """Build a Markov chain from the given model.

    Twenty attempts are made to generate a chain of the given length.
    If the model was build off of insufficient data, the returned chain may be shorter.

    Args:
        model: A dictionary mapping ngrams to possible following words.
        length: The length of the markov chains to generate.
        order: The order of the markov model in use.
        num_chains: The number of chains to generate.

    Returns:
        A list of sentence string markov chain.
    """
    MAX_RETRIES = 20
    chains = []

    for _ in range(num_chains):
        chain = ""
        retries = 0

        while len(chain.split(" ")) < length and retries < MAX_RETRIES:
            new_chain = generate_chain(model, length, order)
            if len(new_chain.split(" ")) > len(chain.split(" ")):
                chain = new_chain
            retries += 1

        chains.append(chain)

    return chains


def generate_chain(model: Dict[str, List[str]], length: int, order: int) -> str:
    """Build a Markov chain from the given model.

    Args:
        model: A dictionary mapping ngrams to possible following words.
        length: The length of the markov chains to generate.
        order: The order of the markov model in use.

    Returns:
        A sentence string markov chain.
    """
    current_ngram = random.choice((list(model)))
    chain = current_ngram.split(" ")

    while len(chain) < length:
        possibilities = model.get(current_ngram)

        if not possibilities:
            break

        next_word = random.choice(possibilities)
        chain.append(next_word)
        current_ngram = " ".join(chain[(-1 * order) :])

    return " ".join(chain)
