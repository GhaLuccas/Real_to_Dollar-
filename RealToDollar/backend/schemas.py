from decimal import Decimal

from pydantic import BaseModel


class RealRequest(BaseModel):
    brl: Decimal


class ConverterResponse(BaseModel):
    brl: Decimal
    usd: Decimal
