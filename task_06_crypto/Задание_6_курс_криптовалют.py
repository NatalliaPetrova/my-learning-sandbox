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
    coin1 = price1_combobox.get().strip()
    coin2 = price2_combobox.get().strip()
    coin3 = price3_combobox.get().strip()

    if coin1 and coin2 and coin3:
        try:
            # ids = ",".join(crypto.keys())
            ids = f"{coin1},{coin2},{coin3}"
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd')
            response.raise_for_status()
            data = response.json()
            if coin1 in data and coin2 in data and coin3 in data:
                price1 = data[coin1]['usd']
                price2 = data[coin2]['usd']
                price3 = data[coin3]['usd']
                name1 = crypto[coin1]
                name2 = crypto[coin2]
                name3 = crypto[coin3]
                mb.showinfo("Курс обмена",
                    f"Курс 1 {name1}  = {price1:.2f} USD\n"                    
                            f"Курс 1 {name2} = {price2:.2f} USD\n"
                            f"Курс 1 {name3} = {price3:.2f} USD")
            else:
                mb.showerror("Ошибка", "Не удалось получить курс для одной или нескольких выбранных монет.")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите криптовалюту")


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