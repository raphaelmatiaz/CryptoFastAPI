from pydantic import BaseModel

class Bitcoin(BaseModel):
    symbol : str
    name : str
    rank : int
    price_usd : float
    market_cap_usd : float
    volume24 : float
    csupply : float


class coinInfo(BaseModel):

    symbol : str
    name : str
    rank : int
    price_usd : float
    price_btc : float
    market_cap_usd : float
    volume24 : float




    #  "id": "80",
    #         "symbol": "ETH",
    #         "name": "Ethereum",
    #         "nameid": "ethereum",
    #         "rank": 2,
    #         "price_usd": "3235.94",
    #         "percent_change_24h": "1.79",
    #         "percent_change_1h": "0.15",
    #         "percent_change_7d": "6.99",
    #         "price_btc": "0.048484",
    #         "market_cap_usd": "395999687569.71",
    #         "volume24": 10029819924.236187,
    #         "volume24a": 9870668879.17391,
    #         "csupply": "122375302.00",
    #         "tsupply": "122375302",
    #         "msupply": ""



