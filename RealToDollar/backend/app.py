from fastapi import FastAPI
from schemas import RealRequest , ConverterResponse
from services import fetch_exchange

main = FastAPI()


@main.get('/')
def hello():
    return {'message': 'Hello word'}


@main.get('/convert', response_class=ConverterResponse)
async def convert(brl : RealRequest = 1.0):
    exchnage_rate = await fetch_exchange
    ...
    