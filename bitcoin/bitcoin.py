import requests
import sys
import json

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    o = response.json()
    amount = n * o["bpi"]["USD"]["rate_float"]
    print(f"${amount:,.4f}")
except requests.RequestException:
    pass

