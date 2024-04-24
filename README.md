# LATEST CRYPTO-DATA API

The **LATEST CRYPTO-DATA API** is an API project built leveraging the renowned **FastAPI** web framework, and was created as my final project for the *'Backend I'*  module from the *'Programacão Web - 23/25'* course at **Escola de Tecnologias, Inovação e Criação do Algarve - ETIC Algarve**.

#
## Goal of this APP

My ambition with this project, was to create an API with multiple endpoints, each retrieving a target pocket of data, relative to a specific aspect of the Cryptocurrency ecosystem. 

Ultimetly, this API may serve as a backend app for providing the latest data to a crypto-aimed dashboard, web-app or website, in which the latest data on prices, rankings, volumes, marketCAP and exchange platforms would be relevant that web serveice's goal.

#
## Why use FastAPI?

**FastAPI** was an obvious choice for this project, first, because it was the API Framework to which I was istroduced in the *'Backend I'*  module from the *'Programacão Web - 23/25'* course at **ETIC Algarve**, and was mandatory in the context of this project option. 

In a broader sence, **FastAPI** is a great choice for building APIs due to it's efficiency and speed, ease of use, and built-in modern features such as the **FastAPI class** and decorator functions (allowing for a smooth and intuitive creation of endpoints) as well as automatic documentation and type hinting. This makes development faster and ensures well-structured, reliable APIs. 

#
## Installation

In order to install the app, execute the following steps in order:



1. ***Cloning the Repository*** : 

Open up the terminal of your choice and **cd** into the location where you'd like to clone the repository, for example: _/desktop_. Then type the following command:
```
     git clone https://github.com/raphaelmatiaz/CryptoFastAPI.git
```
Alteratively, you may also dowload and unzip the repo by clicking the green <**CODE**> button on the top right corner of the repo, and then clicking **Download Zip**.

2. ***Entering the Cloned Repository*** : 

From you current path location, **cd** into the cloned repository:
```
     cd CryptoFastAPI
```
3. ***Installing and Running the APP*** : 

Now that you are in the cloned repository path, start by installing the app via the following command:
```
    make install
```
---------------------
/!\ **NOTE** /!\  
_Make sure **Docker** and **docker-compose** are propperly installed on your system in order for this step to work! 

#
## Using the API Application

The API will be running immedialy after intallation. You can open up a new browser window and acces the following url to start interacting with it:
```
    http://localhost:8000/
```
In order to use the app, simply add any of the following url endpoints to your current root url __localhost:8000/__. Each endpoint will submit an HTTP 'GET' request, and return the latest crypto informations uniquely relative to it in JSON format:

**EXAMPLE** 

```
# Request to endpoint '/bitcoin'

http://localhost:8000/bitcoin
```

```
# Reponse sample from that request

[
  {
    "id": "90",
    "symbol": "BTC",
    "name": "Bitcoin",
    "nameid": "bitcoin",
    "rank": 1,
    "price_usd": "64711.26",
    "percent_change_24h": "-2.65",
    "percent_change_1h": "-0.56",
    "percent_change_7d": "1.37",
    "price_btc": "1.00",
    "market_cap_usd": "1272756915151.50",
    "volume24": 26503101700.7098,
    "volume24a": 27001498893.2909,
    "csupply": "19668246.00",
    "tsupply": "19668246",
    "msupply": "21000000"
  }
]
```


**ENDPOINTS**

*__Raw Response:__*
all the data (untreated)

* **/bitcoin** : Gets the latest information for Bitcoin;

* **/top100** : Gets the latest information for all Altcoins, from rank 2 to  rank 101 (meaning the top 100 cryptocurrencies immediatly after Bitcoin);

* **/exchanges** : Gets the latest information on Crypto Exchange Platforms.

*__Filtered Response:__*
most relevant fields from each endpoint 


* **/bitcoin/filtered** : Gets the following latest information for Bitcoin:

    * Symbol
    * Name
    * Rank
    * Price USD
    * Price BTC
    * Market Cap USD
    * Volume 24h

* **/top100/filtered** : Gets the following information for all Altcoins, from rank 2 to  rank 101 (meaning the top 100 cryptocurrencies immediatly after Bitcoin);

    * Symbol
    * Name
    * Rank
    * Price USD
    * Price BTC
    * Market Cap USD
    * Volume 24h

* **/exchanges/filtered** : Gets the latest information on Crypto Exchange Platforms.

    * Name
    * Volume USD
    * Active_pairs
    * Website URL
    * Country

**START AND STOP THE APP**

/!\ **NOTE** /!\  
Make sure you followed the steps under **Installation** before you use the following commands. You may encounter issues otherwise.

For any subsequent uses of the app:

* Start the app
```
make start
```
* Stop the app
```
make stop
```
Alternatively, you may also access the terminal instance running the app, and use "**CTRL + C**" to terminate the current running process.

**LOGGING MESSAGES**

The APP includes custom logging messages to keep you informed during use. These messages are easily distinguishable as they start with '**INFO:main**' and are encased in little boxes for readability purposes.

They detail each relevant step of a request, providing information encased in helpful messages, such as **status codes** or even **date and time** of each event [Time zone is set to 'Portugal : Lisbon'].

**EXAMPLE** 

```
crypto-1  | INFO:main:==========================================================================
crypto-1  | INFO:main:--------------------------- 24/04/2024 17:26:58---------------------------
crypto-1  | INFO:main: Successfully returned latest Bitcoin data in JSON format! 
crypto-1  | INFO:main: Check 'localhost/8000/bitcoin' to view the response! 
crypto-1  | INFO:main:==========================================================================
```


------------------
------------------