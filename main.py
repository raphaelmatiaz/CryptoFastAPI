#-------------- IMPORTS -----------------------------------------------------------

import requests
from fastapi import FastAPI
import uvicorn
import models
import logging
from datetime import datetime
from pytz import timezone

#==================================================================================
# API Instance

app = FastAPI()

#  -  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   
# Logger Instance & Config

logging.basicConfig(level=logging.INFO)

logger = logger = logging.getLogger(__name__)

#  -  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   
# Date & Time

lisbon_tz = timezone('Europe/Lisbon')

# current date-tiime
now = datetime.now(lisbon_tz)
 
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


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
    logger.info("==========================================================================")
    logger.info(f"--------------------------- {dt_string}---------------------------")
    logger.info(f" HTTP 'GET' request sent to CoinLore endpoint: {bitcoin}")
    logger.info("==========================================================================")



    if result.status_code == 200:
        logger.info("==========================================================================")
        logger.info(f"--------------------------- {dt_string}---------------------------")
        logger.info(f" REQUEST SUCCESS! Result status code : {result.status_code} - OK")
        logger.info("==========================================================================")

        data = result.json()

        logger.info("==========================================================================")
        logger.info(f"--------------------------- {dt_string}---------------------------")
        logger.info(f" Successfully returned latest Bitcoin data in JSON format! ")
        logger.info(f" Check 'localhost/8000/bitcoin' to view the response! ")
        logger.info("==========================================================================")

        return data
    
    else:
        logger.info("==========================================================================")
        logger.info(f"--------------------------- {dt_string}---------------------------")
        logger.info(f" REQUEST FAILED! Result status code : {result.status_code}")
        logger.info(f" Failed to request latest Bitcoin data")
        logger.info("==========================================================================")

# ---------------------------------------------------------------------------------
# Filtered Bitcoin Data


@app.get("/bitcoin/filtered")
def getBitcoinFiltered():

    filteredCoins = []

    coins = getBitcoin()
    
    logger.info("==========================================================================")
    logger.info(f"--------------------------- {dt_string}---------------------------")
    logger.info(f" Innitializing data filter ")
    logger.info("--------------------------------------------------------------------------")
    logger.info("==========================================================================")

    for coin in coins:

        filteredCoin = models.coinInfo(**coin)
        logger.info(f" {coin['name']} data filtered successfully! ")
        filteredCoins.append(filteredCoin)

        logger.info("==========================================================================")
        logger.info(f"--------------------------- {dt_string}---------------------------")
        logger.info(f" Successfully filtered latest Bitcoin data! ")
        logger.info(f" Check 'localhost/8000/bitcoin/filtered' to view the filtered JSON response! ")
        logger.info("==========================================================================")

    return filteredCoins



# ---------------------------------------------------------------------------------
# Raw Exchange Data

allexchanges = 'https://api.coinlore.net/api/exchanges/'

@app.get("/exchanges")
def allExchanges():
    result = requests.get(allexchanges)

    logger.info("==========================================================================")
    logger.info(f"--------------------------- {dt_string}---------------------------")
    logger.info(f" HTTP 'GET' request sent to CoinLore endpoint: {allexchanges}")
    logger.info("==========================================================================")


    if result.status_code == 200:

        logger.info("==========================================================================")
        logger.info(f"--------------------------- {dt_string}---------------------------")
        logger.info(f" REQUEST SUCCESS! Result status code : {result.status_code} - OK")
        logger.info("==========================================================================")

        data = result.json()

        logger.info("==========================================================================")
        logger.info(f"--------------------------- {dt_string}---------------------------")
        logger.info(f" Successfully returned latest Exchanges data in JSON format! ")
        logger.info(f" Check 'localhost/8000/exchanges' to view the response! ")
        logger.info("==========================================================================")

        return data

    else:
        logger.info("==========================================================================")
        logger.info(f"--------------------------- {dt_string}---------------------------")
        logger.info(f" REQUEST FAILED! Result status code : {result.status_code}")
        logger.info(f" Failed to request latest Exchanges data")
        logger.info("==========================================================================")

# ---------------------------------------------------------------------------------
# Filtered Exchange Data

@app.get("/exchanges/filtered")
def filterExchangeData():

    filtered_exchanges = []

    all_exchanges = allExchanges()

    logger.info("==========================================================================")
    logger.info(f"--------------------------- {dt_string}---------------------------")
    logger.info(f" Innitializing data filter ")
    logger.info("--------------------------------------------------------------------------")
    logger.info("==========================================================================")


    for exchange_id, exchange_details in all_exchanges.items():

        filtered_exchange = models.exchangeInfo(**exchange_details)
        logger.info(f" {exchange_details['name']} data filtered successfully! ")
        filtered_exchanges.append(filtered_exchange)

    logger.info("==========================================================================")
    logger.info(f"--------------------------- {dt_string}---------------------------")
    logger.info(f" Successfully filtered latest Exchanges data! ")
    logger.info(f" Check 'localhost/8000/exchanges/filtered' to view the filtered JSON response! ")
    logger.info("==========================================================================")

    return filtered_exchanges

# ---------------------------------------------------------------------------------
# Raw 2-101Rank Data (ETH to 101rank)


top100 = 'https://api.coinlore.net/api/tickers/?start=1&limit=100'

@app.get("/top100")
def crypto100():
    result = requests.get(top100)

    logger.info("==========================================================================")
    logger.info(f"--------------------------- {dt_string}---------------------------")
    logger.info(f" HTTP 'GET' request sent to CoinLore endpoint: {top100}")
    logger.info("==========================================================================")


    if result.status_code == 200:

        logger.info("==========================================================================")
        logger.info(f"--------------------------- {dt_string}---------------------------")
        logger.info(f" REQUEST SUCCESS! Result status code : {result.status_code} - OK")
        logger.info("==========================================================================")

        data = result.json()

        logger.info("==========================================================================")
        logger.info(f"--------------------------- {dt_string}---------------------------")
        logger.info(f" Successfully returned latest Top100 altoins data in JSON format! ")
        logger.info(f" Check 'localhost/8000/top100' to view the response! ")
        logger.info("==========================================================================")

        return data
    
    else:
        logger.info("==========================================================================")
        logger.info(f"--------------------------- {dt_string}---------------------------")
        logger.info(f" REQUEST FAILED! Result status code : {result.status_code}")
        logger.info(f" Failed to request latest Top100 alticoins data")
        logger.info("==========================================================================")


# ---------------------------------------------------------------------------------
# Filtered 2-101Rank Data (ETH to 101rank)


@app.get("/top100/filtered")
def filterCoinData():

    filteredCoins = []

    coins = crypto100()['data']

    logger.info("==========================================================================")
    logger.info(f"--------------------------- {dt_string}---------------------------")
    logger.info(f" Innitializing data filter ")
    logger.info("--------------------------------------------------------------------------")
    logger.info("==========================================================================")
    
    for coin in coins:

        filteredCoin = models.coinInfo(**coin)
        logger.info(f" {coin['name']} data filtered successfully! ")
        filteredCoins.append(filteredCoin)

    logger.info("==========================================================================")
    logger.info(f"--------------------------- {dt_string}---------------------------")
    logger.info(f" Successfully filtered latest Top100 altcoins data! ")
    logger.info(f" Check 'localhost/8000/top100/filtered' to view the filtered JSON response! ")
    logger.info("==========================================================================")

    return filteredCoins


# ---------------------------------------------------------------------------------
#APP START

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

