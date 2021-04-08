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


class TestMetaStatsClient:
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
