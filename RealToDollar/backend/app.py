from decimal import Decimal

from fastapi import (
    FastAPI,
    HTTPException,
    status,
)
from schemas import BRLCurencyRequest, USDConvertedResponse
from services.fetch_exchange import get_exchange_rate

app = FastAPI()


@app.get('/')
def hello():
    return {'message': 'Hello word'}


@app.post('/convert', response_model=USDConvertedResponse)
async def convert(brl: BRLCurencyRequest):
    try:
        exchange_rate = await get_exchange_rate()
        usd_value = brl.amount * exchange_rate
        usd_value_rounded = usd_value.quantize(Decimal('0.01'))
        return {
            'brl_amount': brl.amount,
            'usd_converted': usd_value_rounded,
            'exchange_rate_message': f'{brl.amount} USD = {usd_value_rounded} BRL',
        }
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Invalid input: Amount must be a decimal.',
        )
