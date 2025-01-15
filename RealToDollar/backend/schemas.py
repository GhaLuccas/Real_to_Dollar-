from decimal import Decimal

from pydantic import BaseModel


class BRLCurencyRequest(BaseModel):
    amount: Decimal


class USDConvertedResponse(BaseModel):
    brl_amount: Decimal
    usd_converted: Decimal
    exchange_rate_message: str
