from pydantic import BaseModel

class Bitcoin(BaseModel):
    symbol : str
    name : str
    rank : int
    price_usd : float
    market_cap_usd : float
    volume24 : float
    csupply : float



