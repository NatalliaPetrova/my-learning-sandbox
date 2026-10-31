from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_price1_label(event):
    code = price1_combobox.get()
    name = crypto[code]
    price1_label.config(text=name)


def update_price2_label(event):
    code = price2_combobox.get()
    name = crypto[code]
    price2_label.config(text=name)


def update_price3_label(event):
    code = price3_combobox.get()
    name = crypto[code]
    price3_label.config(text=name)


def exchange():
    pass


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

# Создание графического интерфейса
window = Tk()
window.title("Курс криптовалют")
window.geometry("360x380")

Label(text="Криптовалюта 1:").pack(padx=10, pady=5)
price1_combobox = ttk.Combobox(values=list(crypto.keys()), state="readonly")
price1_combobox.pack(padx=10, pady=5)
price1_combobox.bind("<<ComboboxSelected>>",  update_price1_label)

price1_label = ttk.Label()
price1_label.pack(padx=10, pady=10)

Label(text="Криптовалюта 2:").pack(padx=10, pady=5)
price2_combobox = ttk.Combobox(values=list(crypto.keys()), state="readonly")
price2_combobox.pack(padx=10, pady=5)
price2_combobox.bind("<<ComboboxSelected>>", update_price2_label)

price2_label = ttk.Label()
price2_label.pack(padx=10, pady=10)

Label(text="Криптовалюта 3:").pack(padx=10, pady=5)
price3_combobox = ttk.Combobox(values=list(crypto.keys()), state="readonly")
price3_combobox.pack(padx=10, pady=5)
price3_combobox.bind("<<ComboboxSelected>>", update_price3_label)

price3_label = ttk.Label()
price3_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена криптовалюты к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()