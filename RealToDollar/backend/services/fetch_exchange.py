from decimal import Decimal

import httpx

EXCHANGE_API_URL = 'https://api.exchangerate-api.com/v4/latest/usd'


async def get_exchange_rate() -> Decimal:
    async with httpx.AsyncClient() as client:
        response = await client.get(EXCHANGE_API_URL)
        data = response.json()
        try:
            rate = Decimal(data['rates']['BRL'])
        except (KeyError, ValueError, TypeError) as e:
            raise ValueError(f'Invalid exchange rate data: {data}') from e
        return rate
