#-------------- IMPORTS -----------------------------------------------------------

import requests
import json
from fastapi import FastAPI
import uvicorn
import models
import logging

#==================================================================================

app = FastAPI()

logger = logger = logging.getLogger(__name__)

# Root of API


#============== API ENDPOINTS =====================================================

# ---------------------------------------------------------------------------------
# Root

@app.get('/')
def root():
    return {"|| Raw Bitcoin Data => /bitcoin || Filtered Bitcoin Data => /bitcoin/filtered || Raw Top 100 crypto data => /top100 || Filtered Top 100 crypto data => /top100/filtered || Raw Exchanges Data => /exchanges || Filtered Exchanges Data => /exchanges/filtered ||  "}



# ---------------------------------------------------------------------------------
# Raw Bitcoin Data

bitcoin = 'https://api.coinlore.net/api/ticker/?id=90'

@app.get("/bitcoin")
def getBitcoin():
    result = requests.get(bitcoin)


    if result.status_code == 200:
        data = result.json()
        
        print(data)

        return data
    
    else:
        print(f"Error status code {result.status_code}")

# ---------------------------------------------------------------------------------
# Filtered Bitcoin Data


@app.get("/bitcoin/filtered")
def getBitcoinFiltered():

    filteredCoins = []

    coins = getBitcoin()
    
    for coin in coins:

        filteredCoin = models.coinInfo(**coin)
        print(filteredCoin)
        filteredCoins.append(filteredCoin)

    return filteredCoins



# ---------------------------------------------------------------------------------
# Raw Exchange Data

allexchanges = 'https://api.coinlore.net/api/exchanges/'

@app.get("/exchanges")
def allExchanges(datafile='exchanges.json'):
    result = requests.get(allexchanges)


    if result.status_code == 200:
        data = result.json()
        print('success!')
        print(data)

        return data

    else:
        print(f"Error status code {result.status_code}")

# ---------------------------------------------------------------------------------
# Filtered Exchange Data

@app.get("/exchanges/filtered")
def filterExchangeData():

  filtered_exchanges = []

  all_exchanges = allExchanges()


  for exchange_id, exchange_details in all_exchanges.items():

    filtered_exchange = models.exchangeInfo(**exchange_details)
    filtered_exchanges.append(filtered_exchange)


  return filtered_exchanges

# ---------------------------------------------------------------------------------
# Raw 2-101Rank Data (ETH to 101rank)


top100 = 'https://api.coinlore.net/api/tickers/?start=1&limit=100'

@app.get("/top100")
def crypto100(datafile='top100.json'):
    result = requests.get(top100)


    if result.status_code == 200:
        data = result.json()
        print('success!')
        print(data)

        return data
    
    else:
        print(f"Error status code {result.status_code}")


# ---------------------------------------------------------------------------------
# Filtered 2-101Rank Data (ETH to 101rank)


@app.get("/top100/filtered")
def filterCoinData():

    filteredCoins = []

    coins = crypto100()['data']
    
    for coin in coins:

        filteredCoin = models.coinInfo(**coin)
        print(filteredCoin)
        filteredCoins.append(filteredCoin)

    return filteredCoins


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# ---------------------------------------------------------------------------------