from .metaStats_models import Metrics


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
        """Returns metrics of MetaApi account
        https://metastats-api-v1.agiliumtrade.agiliumtrade.ai/swagger/#!
        /default/get_users_current_accounts_accountId_metrics

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
