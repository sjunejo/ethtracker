import asyncio
from contextlib import suppress


from web.ethdata import get_eth_gbp, get_eth_usd

timeout = 5.0

async def __get_eth_prices():
    while True:
        print("ETH/USD: $" + get_eth_usd())
        print("ETH/GBP: £" + get_eth_gbp())
        await asyncio.sleep(5)


def start_eth_price_loop():
    task = asyncio.Task(__get_eth_prices())
    loop = asyncio.get_event_loop()

    with suppress(asyncio.CancelledError):
        loop.run_until_complete(task)