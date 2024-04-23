import requests
import json
from fastapi import FastAPI
import uvicorn


app = FastAPI()

# Root of API

@app.get('/')
def root():
    return {"||      Bitcoin => /bitcoin     ||       Top 100 cryptos => /top100      ||        Exchanges => /exchanges     ||  "}

# Gets Bitcoin data and dumps it into json
bitcoin = 'https://api.coinlore.net/api/ticker/?id=90'

@app.get("/bitcoin")
def getBitcoin(datafile='bitcoin.json'):
    result = requests.get(bitcoin)


    if result.status_code == 200:
        data = result.json()
        print('success!')
        print(data)

        with open(datafile, 'w') as outfile:
            json.dump(data, outfile, indent=4)
        print("JSON DUMPED")
        print("JSON DUMPED")
        print("JSON DUMPED")
        print("JSON DUMPED")
        print("BITCOIN")

    else:
        print(f"Error status code {result.status_code}")

    return result



# Gets and dumps data relative to all exchanges
allexchanges = 'https://api.coinlore.net/api/exchanges/'

@app.get("/exchanges")
def allExchanges(datafile='exchanges.json'):
    result = requests.get(allexchanges)


    if result.status_code == 200:
        data = result.json()
        print('success!')
        print(data)

        with open(datafile, 'w') as outfile:
            json.dump(data, outfile, indent=4)
        print("JSON DUMPED")
        print("JSON DUMPED")
        print("JSON DUMPED")
        print("JSON DUMPED")
        print("ALL EXCHANGES")

    else:
        print(f"Error status code {result.status_code}")

    return result


# Gets and dumps crypto data from ETH to 101's position
top100 = 'https://api.coinlore.net/api/tickers/?start=1&limit=100'

@app.get("/top100")
def crypto100(datafile='top100.json'):
    result = requests.get(top100)


    if result.status_code == 200:
        data = result.json()
        print('success!')
        print(data)

        with open(datafile, 'w') as outfile:
            json.dump(data, outfile, indent=4)
        print("JSON DUMPED")
        print("JSON DUMPED")
        print("JSON DUMPED")
        print("JSON DUMPED")
        print("TOP 100 CRYPTO")

    else:
        print(f"Error status code {result.status_code}")

        return result



if __name__ == '__main__':
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)