import requests
import time
import json


def btc():
    old_price = 1
    while True:
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url).json()
        time_updated = response['time']['updated']
        rate_price = float(response['bpi']['USD']['rate_float'])
        ratio = (rate_price - old_price) / old_price * 100
        print("\n\n" + time_updated + "\nbtc/dollar: " + str(rate_price) + "\nratio: %" + str(ratio))
        old_price = rate_price
        time.sleep(60)

btc()
