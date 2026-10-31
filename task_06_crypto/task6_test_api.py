import requests
import pprint
import json
# проверка какие есть монеты в топе чтобы собрать для них словарь
url_top = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=15&page=1"

data_top = requests.get(url_top).json()

for coin in data_top:
    print(f'"{coin["id"]}": "{coin["name"]} ({coin["symbol"].upper()})",')

#Словарь топ 10 криптовалют и их полных названий
crypto = {
    "bitcoin": "Bitcoin (BTC)",
    "ethereum": "Ethereum (ETH)",
    "tether": "Tether (USDT)",
    "binancecoin": "BNB (BNB)",
    "ripple": "XRP (XRP)",
    "usd-coin": "USDC (USDC)",
    "solana": "Solana (SOL)",
    "tron": "TRON (TRX)",
    "dogecoin": "Dogecoin (DOGE)",
    "zcash": "Zcash (ZEC)"
}

ids = ",".join(crypto.keys())
# проверяю, что API отдает цены для  словаря
url_price = (f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd")
data_price = requests.get(url_price).json()
p = pprint.PrettyPrinter(indent=4)
p.pprint(data_price)
