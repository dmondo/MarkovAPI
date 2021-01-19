Markov API
==========

For the client, see `this repo <https://github.com/dmondo/MarkovBot>`_.
The Markov API provides an endpoint to generate Markov models from passed text.

Usage
-----

Provide the '/' endpoint with: a 'text' parameter contained the text you would like modeled,
and an 'order' parameter specifying the order of the n-grams model to be generated.

When hosted locally, the API defaults to port 5000.

.. code-block:: console

   $ curl -i -H localhost:5000/?text=sample&order=3

.. toctree::
   :hidden:
   :maxdepth: 1

   license
