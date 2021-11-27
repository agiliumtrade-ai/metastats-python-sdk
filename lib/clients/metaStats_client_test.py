import pytest
import respx
from httpx import Response
from .httpClient import HttpClient
from .metaStats_client import MetaStatsClient

METASTATS_API_URL = 'https://metastats-api-v1.agiliumtrade.agiliumtrade.ai'
token = 'header.payload.sign'
expected = {
    'trades': 10,
    'equity': 10102.5,
    'balance': 10105,
    'profit': 104,
    'deposits': 10001
}
account_id = '1234567'
httpClient = HttpClient()
metastats_client = MetaStatsClient(httpClient, token)


class TestGetMetrics:
    @respx.mock
    @pytest.mark.asyncio
    async def test_retrieve_metrics(self):
        """Should retrieve account metrics from API."""
        rsps = respx.get(f'{METASTATS_API_URL}/users/current/accounts/{account_id}/metrics?'
                         f'includeOpenPositions=false') \
            .mock(return_value=Response(200, json={'metrics': expected}))
        profiles = await metastats_client.get_metrics(account_id)
        assert rsps.calls[0].request.url == \
            f'{METASTATS_API_URL}/users/current/accounts/{account_id}/metrics?includeOpenPositions=false'
        assert rsps.calls[0].request.method == 'GET'
        assert rsps.calls[0].request.headers['auth-token'] == token
        assert profiles == expected

    @respx.mock
    @pytest.mark.asyncio
    async def test_retrieve_metrics_with_open_positions(self):
        """Should retrieve account metrics with included open positions from API."""
        rsps = respx.get(f'{METASTATS_API_URL}/users/current/accounts/{account_id}/metrics?'
                         f'includeOpenPositions=true') \
            .mock(return_value=Response(200, json={'metrics': expected}))
        profiles = await metastats_client.get_metrics(account_id, True)
        assert rsps.calls[0].request.url == \
            f'{METASTATS_API_URL}/users/current/accounts/{account_id}/metrics?includeOpenPositions=true'
        assert rsps.calls[0].request.method == 'GET'
        assert rsps.calls[0].request.headers['auth-token'] == token
        assert profiles == expected


start_time = '2020-01-01 00:00:00.000'
end_time = '2021-01-01 00:00:00.000'


class TestGetTrades:

    @respx.mock
    @pytest.mark.asyncio
    async def test_retrieve_account_trades(self):
        """Should retrieve account trades from API."""
        rsps = respx.get(f'{METASTATS_API_URL}/users/current/accounts/{account_id}/historical-trades/'
                         f'{start_time}/{end_time}') \
            .mock(return_value=Response(200, json={'trades': expected}))
        trades = await metastats_client.get_account_trades(account_id, start_time, end_time)
        assert rsps.calls[0].request.url == \
            f'{METASTATS_API_URL}/users/current/accounts/{account_id}/historical-trades/2020-01-01%2000:00:00.000' \
            '/2021-01-01%2000:00:00.000?updateHistory=false&limit=1000&offset=0'
        assert rsps.calls[0].request.method == 'GET'
        assert rsps.calls[0].request.headers['auth-token'] == token
        assert trades == expected


class TestGetOpenTrades:

    @respx.mock
    @pytest.mark.asyncio
    async def test_retrieve_account_open_trades(self):
        """Should retrieve account open trades from API."""
        rsps = respx.get(f'{METASTATS_API_URL}/users/current/accounts/{account_id}/open-trades') \
            .mock(return_value=Response(200, json={'openTrades': expected}))
        open_trades = await metastats_client.get_account_open_trades(account_id)
        assert rsps.calls[0].request.url == \
            f'{METASTATS_API_URL}/users/current/accounts/{account_id}/open-trades'
        assert rsps.calls[0].request.method == 'GET'
        assert rsps.calls[0].request.headers['auth-token'] == token
        assert open_trades == expected
