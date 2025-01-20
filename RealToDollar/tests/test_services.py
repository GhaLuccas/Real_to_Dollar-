from decimal import Decimal

import pytest

from backend.services.fetch_exchange import EXCHANGE_API_URL, get_exchange_rate

MOCK_API_RESPONSE = {
    'provider': 'https://www.exchangerate-api.com',
    'base': 'USD',
    'date': '2025-01-14',
    'rates': {
        'USD': 1,
        'BRL': 6.1,
        'EUR': 0.93,
    },
}


@pytest.mark.asyncio
async def test_get_exchange_rate(mocker):
    mock_get = mocker.patch(
        'backend.services.fetch_exchange.httpx.AsyncClient.get'
    )
    mock_get.return_value.json = mocker.Mock(return_value=MOCK_API_RESPONSE)

    exchange_rate = await get_exchange_rate()

    assert exchange_rate.quantize(Decimal('0.01')) == Decimal('6.1')
    mock_get.assert_called_once_with(EXCHANGE_API_URL)
