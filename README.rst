MetaStats forex metrics API
###########################
MetaStats is a fast, cost-efficient, easy to use and standards-driven cloud forex trading statistics API supporting
both MetaTrader 4 and MetaTrader 5 platforms designed to boost forex application development process.

Using MetaStats API you can develop applications similar to Myfxbook or MetriX extremely fast, saving time you
otherwise spend for coding, optimizing and testing your own trading metrics calculation engine, since we already
did it for you.

MetaStats API is a member of MetaApi project (`https://metaapi.cloud <https://metaapi.cloud>`_), a powerful cloud forex
trading API which supports both MetaTrader 4 and MetaTrader 5 platforms.

MetaStats API features
======================
Features supported:

- support for MetaTrader 4 and MetaTrader 5 platforms
- metrics calculation for MetaTrader accounts added to MetaApi
- optionally include open positions in metrics calculation

The features described above are available for use via a professional, fast, easy to use, standards-driven REST API
which can be easily consumed from any programming language.

The primary intended use of MetaStats API is creating trade monitoring applications.

Pricing
=======
MetaStats is available to all MetaApi users without extra charges at this point.

You pay a fee executing MetaTrader terminal on MetaApi cloud. See
`https://metaapi.cloud/#pricing <https://metaapi.cloud/#pricing>`_ for more details.

MetaApi provides a free tier so that you can test our APIs without any charges.

Frequently asked questions (FAQ)
================================
FAQ is located here: `http://metaapi.cloud/docs/metastats/faq <http://metaapi.cloud/docs/metastats/faq>`_

REST API documentation
======================
MetaStats SDK is built on top of MetaStats REST API.

MetaStats REST API docs are available at
`https://metaapi.cloud/docs/metastats/ <https://metaapi.cloud/docs/metastats/>`_

Code examples
=============
We published some code examples in our github repository, namely:

- Python: `https://github.com/agiliumtrade-ai/metastats-python-sdk/tree/master/examples <https://github.com/agiliumtrade-ai/metastats-python-sdk/tree/master/>`_

Installation
============
.. code-block:: bash

    pip install metaapi-cloud-sdk

Retrieving API token
====================
Please visit `https://app.metaapi.cloud/token <https://app.metaapi.cloud/token>`_ web UI to obtain your API token.

Configuring trading statistics
==============================
.. code-block:: python

    from metaapi_cloud_sdk import MetaStats

    token = '...'
    api = MetaStats(token=token)

See in-code documentation for full definition of possible configuration options.

Retrieving trading statistics
=============================
.. code-block:: python

    account_id = '...'  #  MetaApi account id

    # retrieve MetaApi MetaTrader account statistics
    print(await metaStats.get_metrics(account_id=account_id))

    # retrieve MetaApi MetaTrader account statistics including open positions
    print(await metaStats.get_metrics(account_id=account_id, include_open_positions=True))

Quotas and rate limits
======================
API calls you make are subject to rate limits. See `https://metaapi.cloud/docs/metastats/rateLimiting/ <https://metaapi.cloud/docs/metastats/rateLimiting/>`_ for more details.

Related projects:
=================
See our website for the full list of APIs and features supported `https://metaapi.cloud/#features <https://metaapi.cloud/#features>`_

Some of the APIs you might decide to use together with this module:

1. MetaApi cloud forex trading API `https://metaapi.cloud/docs/client/ <https://metaapi.cloud/docs/client/>`_
2. CopyFactory copy trading  API `https://metaapi.cloud/docs/copyfactory/ <https://metaapi.cloud/docs/copyfactory/>`_
3. MetaTrader account management API `https://metaapi.cloud/docs/provisioning/ <https://metaapi.cloud/docs/provisioning/>`_
