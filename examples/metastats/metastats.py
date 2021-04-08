from lib import MetaStats
import asyncio
import os


async def get_account_metrics():
    # your MetaApi API token
    token = os.getenv('TOKEN') or '<put in your token here>'
    # your MetaApi account id
    account_id = os.getenv('ACCOUNT_ID') or '<put in your account id here>'

    meta_stats = MetaStats(token)
    # you can configure http client via second parameter,
    # see in-code documentation for full definition of possible configuration options

    try:
        metrics = await meta_stats.get_metrics(account_id)
        print(metrics)  # -> {'trades': ..., 'balance': ..., ...}
    except Exception as err:
        print(meta_stats.format_error(err))
    exit(0)

asyncio.run(get_account_metrics())
