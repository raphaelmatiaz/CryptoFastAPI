# LATEST CRYPTO-DATA API

The **LATEST CRYPTO-DATA API** is an API project built leveraging the renowned **FastAPI** web framework, and was created as my final project for the *'Backend I'*  module from the *'Programacão Web - 23/25'* course from **ETIC Algarve** school.

#
## Goal of this APP

My ambition with this project, was to create an API with multiple endpoints, each retrieving a target pocket of data, relative to a specific aspect of the Cryptocurrency ecosystem. 

Ultimetly, this API could serve as a backend app for providing the latest data to a crypto-aimed dashboard, web-app or website of some sort, in which the latest data on prices, rankings and exchange platforms would be relevant to it' goal.

#
## Why use FastAPI?

**FastAPI** was an obvious choice for this project, first, because it was the API Framework to which I was istroduced in the *'Backend I'*  module from the *'Programacão Web'* course at **ETIC Algarve**, and was mandatory in the context of this project option. 

In a broader sence, **FastAPI** is a great choice for building APIs due to it's efficiency and speed, ease of use, and built-in modern features such as the **FastAPI class** and decorator functions (allowing for a smooth and intuitive creation of endpoints) as well as automatic documentation and type hinting. This makes development faster and ensures well-structured, reliable APIs. 

#
## Installation

In order to install the app, execute the following steps in order:



1. ***Cloning the Repository***: 

Open up the terminal of your choice and **cd** into the location where you'd like to clone the repository, for example: _/desktop_. Then type the following command:

     git clone https://github.com/raphaelmatiaz/CryptoFastAPI.git

2. ***Entering the Cloned Repository***: 

From you current path location, **cd** into the cloned repository:

     cd CryptoFastAPI

3. ***Running the APP***: 

Now that you are in the cloned repository, you are able to run the app with the following command:

    make cryptodata

---------------------
/!\ **NOTE** /!\  
_Make sure **Docker** and **docker-compose** are propperly installed on your system in order for this step to work._

#
## Using the API Application

After going throught the **Installation** steps, open up a new browser window and acces the following url:

    http://localhost:8000/

In order to use the app, simply add any of the following url endpoints to your current root url. Each endpoint will return the latest crypto informations uniquely relative to it in JSON format:

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
    * Eank
    * Price USD
    * Price BTC
    * Market Cap USD
    * Volume 24h

* **/top100/filtered** : Gets the following information for all Altcoins, from rank 2 to  rank 101 (meaning the top 100 cryptocurrencies immediatly after Bitcoin);

    * Symbol
    * Name
    * Eank
    * Price USD
    * Price BTC
    * Market Cap USD
    * Volume 24h

* **/exchanges/filtered** : Gets the latest information on Crypto Exchange Platforms.

    * Name
    * Volume USD
    * Active_pairs
    * Price BTC
    * Website URL
    * Country


------------------
------------------