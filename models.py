from pydantic import BaseModel


class coinInfo(BaseModel):

    symbol : str
    name : str
    rank : int
    price_usd : float
    price_btc : float
    market_cap_usd : float
    volume24 : float




class exchangeInfo(BaseModel):

    name : str
    volume_usd : float
    active_pairs : int
    url : str
    country : str



