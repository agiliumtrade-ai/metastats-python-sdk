import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

install_requires = ['typing-extensions~=3.10.0.0', 'iso8601', 'pytz', 'httpx==0.23.0']

tests_require = ['pytest==6.2.5', 'pytest-mock==3.8.2', 'pytest-asyncio==0.16.0', 'mock==4.0.3', 'respx==0.19.2',
                 'freezegun==1.0.0']

setuptools.setup(
    name="metaapi_cloud_metastats_sdk",
    version="3.2.1",
    author="Agilium Labs LLC",
    author_email="agiliumtrade@agiliumtrade.ai",
    description="Python SDK for MetaStats forex trading statistics API. Can calculate metrics for MetaTrader "
                "accounts added to MetaApi. Supports both MetaTrader 5 (MT5) and MetaTrader 4 (MT4). "
                "(https://metaapi.cloud)",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    keywords=['metaapi.cloud', 'MetaTrader', 'MetaTrader 5', 'MetaTrader 4', 'MetaTrader5', 'MetaTrader4', 'MT', 'MT4',
              'MT5', 'forex', 'API', 'REST', 'client', 'sdk', 'cloud', 'metrics', 'MetaStats', 'metastats'],
    url="https://github.com/agiliumtrade-ai/metaapi-metastats-python-sdk",
    include_package_data=True,
    package_dir={'metaapi_cloud_metastats_sdk': 'lib'},
    packages=['metaapi_cloud_metastats_sdk'],
    install_requires=install_requires,
    tests_require=tests_require,
    license='SEE LICENSE IN LICENSE',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
