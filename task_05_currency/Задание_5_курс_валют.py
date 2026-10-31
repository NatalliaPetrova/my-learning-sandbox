from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_base1_label(event):
    code = base1_combobox.get()
    name = currencies[code]
    base1_label.config(text=name)


def update_base2_label(event):
    code = base2_combobox.get()
    name = currencies[code]
    base2_label.config(text=name)


def update_target_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def exchange():
    target_code = target_combobox.get().strip()
    base1_code = base1_combobox.get().strip()
    base2_code = base2_combobox.get().strip()

    if target_code and base1_code and base2_code:
        try:
            response1 = requests.get(f'https://open.er-api.com/v6/latest/{base1_code}')
            response1.raise_for_status()
            data1 = response1.json()
            response2 = requests.get(f'https://open.er-api.com/v6/latest/{base2_code}')
            response2.raise_for_status()
            data2 = response2.json()
            if data1.get('result') != 'success' or data2.get('result') != 'success':
                mb.showerror("Ошибка", "Не удалось получить курсы валют (сбой API)")
                return
            if target_code in data1['rates'] and target_code in data2['rates']:
                exchange_rate1 = data1['rates'][target_code]
                exchange_rate2 = data2['rates'][target_code]
                base1 = currencies[base1_code]
                base2 = currencies[base2_code]
                target = currencies[target_code]
                mb.showinfo("Курс обмена",
                        f"Курс {exchange_rate1:.2f} {target} за 1 {base1}\n"
                                f"Курс {exchange_rate2:.2f} {target} за 1 {base2}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")


# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x360")

Label(text="Базовая валюта 1:").pack(padx=10, pady=5)
base1_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
base1_combobox.pack(padx=10, pady=5)
base1_combobox.bind("<<ComboboxSelected>>", update_base1_label)

base1_label = ttk.Label()
base1_label.pack(padx=10, pady=10)

Label(text="Базовая валюта 2:").pack(padx=10, pady=5)
base2_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
base2_combobox.pack(padx=10, pady=5)
base2_combobox.bind("<<ComboboxSelected>>", update_base2_label)

base2_label = ttk.Label()
base2_label.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_target_label)

target_label = ttk.Label()
target_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()