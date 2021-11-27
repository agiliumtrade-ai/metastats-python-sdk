from .metaStats_models import Metrics, Trade, OpenTrade


class MetaStatsClient:
    """metaapi.cloud MetaStats MetaTrader API client"""
    def __init__(self, http_client, token: str, domain: str = None):
        """Inits MetaTrader API client instance.

        Args:
            http_client: HTTP client.
            token: Authorization token.
            domain: Domain to connect to, default is agiliumtrade.agiliumtrade.ai.
        """
        domain = domain or 'agiliumtrade.agiliumtrade.ai'
        self._httpClient = http_client
        self._host = f'https://metastats-api-v1.{domain}'
        self._token = token

    async def get_metrics(self, account_id: str, include_open_positions: bool = False) -> Metrics:
        """Returns metrics of MetaApi account. This API call is billable
        https://metaapi.cloud/docs/metastats/restApi/api/calculateMetrics/

        Args:
            account_id: MetaApi account id.
            include_open_positions: Indicates whether open positions will be included in the metrics, default false.

        Returns:
            Account metrics.
        """
        opts = {
            'url': f'{self._host}/users/current/accounts/{account_id}/metrics',
            'method': 'GET',
            'params': {
                'includeOpenPositions': include_open_positions
            },
            'headers': {
                'auth-token': self._token
            }
        }
        response = await self._httpClient.request(opts)
        return response['metrics']

    async def get_account_trades(self, account_id: str, start_time: str, end_time: str, update_history: bool = False,
                                 limit: int = 1000, offset: int = 0) -> Trade:
        """Returns historical trades of MetaApi account.
        https://metaapi.cloud/docs/metastats/restApi/api/getHistoricalTrades/

        Args:
            account_id: MetaApi account id.
            start_time: Start of time range, inclusive.
            end_time: End of time range, exclusive.
            update_history: Update historical trades before returning results. If set to true, the API call will be
            counted towards billable MetaStats API calls. If set to false, the API call is not billable.
            limit: Pagination limit.
            offset: Pagination offset.

        Returns:
            Account historical trades.
        """
        opts = {
            'url': f'{self._host}/users/current/accounts/{account_id}/historical-trades/{start_time}/{end_time}',
            'method': 'GET',
            'params': {
                'updateHistory': update_history,
                'limit': limit,
                'offset': offset
            },
            'headers': {
                'auth-token': self._token
            }
        }
        response = await self._httpClient.request(opts)
        return response['trades']

    async def get_account_open_trades(self, account_id: str) -> OpenTrade:
        """Returns open trades of MetaApi account. This API call is not billable.
        https://metaapi.cloud/docs/metastats/restApi/api/getOpenTrades/

        Args:
            account_id: MetaApi account id.

        Returns:
            Account historical trades.
        """
        opts = {
            'url': f'{self._host}/users/current/accounts/{account_id}/open-trades',
            'method': 'GET',
            'headers': {
                'auth-token': self._token
            }
        }
        response = await self._httpClient.request(opts)
        return response['openTrades']
