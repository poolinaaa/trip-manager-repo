import datetime
import config as c
import requests
import json
import tkinter as tk
from tkinter import *
from sqlite3 import *
import csv

import sqlite3 as sql
import json
import requests

from datetime import datetime




def preparingData(data: dict, codeCurrency):
    c.dates = [date for date in data['rates']]
    c.rate = [data['rates'][date][codeCurrency] for date in data['rates']]
    c.eur = [data['rates'][date]['EUR'] for date in data['rates']]
    c.usd = [data['rates'][date]['USD'] for date in data['rates']]
    c.pln = [data['rates'][date]['PLN'] for date in data['rates']]
    c.cny = [data['rates'][date]['CNY'] for date in data['rates']]


def checkDate(date):
    try:
        isDateCorrect = datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
        return False


def confirmButton(frame, dateStart, dateEnd, baseCurrName, codeCurrency, fake1, fake2, fake3, btn1, btn2, btn3):

    start = dateStart.get()
    end = dateEnd.get()
    if (checkDate(start) and checkDate(end)):
        params = {'start_date': start, 'end_date': end,
                  'base': baseCurrName, 'symbols': f'{codeCurrency},EUR,USD,PLN,CNY'}
        r = requests.get('https://api.exchangerate.host/timeseries/', params)
        print(r)
        try:
            currencyData = r.json()
        except json.JSONDecodeError:
            print('Wrong format of c.currencyData.')
        else:
            print(currencyData)
            preparingData(currencyData, codeCurrency)
            fake1.destroy()
            fake2.destroy()
            fake3.destroy()
            btn1.grid(column=0, row=1, padx=15, pady=10)
            btn2.grid(column=0, row=1, padx=15, pady=10)
            btn3.grid(column=0, row=1, padx=15, pady=10)

    else:
        incorrectDate = tk.Label(
            master=frame, text='wrong format of date, try again', font=c.errorFont, bg=c.highlight, fg='white')
        incorrectDate.pack()
        frame.after(5000, incorrectDate.destroy)
