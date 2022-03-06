import datetime
import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk,PhotoImage
import webbrowser
import time

brasov = ('45', '25')
constanta = ('44', '28')
bucuresti = ('44', '26')
cluj = ('46', '23')
oradea = ('47', '21')
sibiu = ('45', '24')
timisoara = ('45', '21')
lat = '44'
lon = '28'
oras = "Constanta"
final_info = ''
final_data1 = ''
conditions = ['a']
pic = ''
counter = 0
articles = []
my_urls = []
xurl = ''

time1 = datetime.datetime.now()
root = tk.Tk()
root.geometry('1000x670')
root.resizable(width=False, height=False)
root.title('News App')

def getNews():
    global xurl
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()
    ron = data['rates']['RON']
    usd = data['rates']['USD']
    gbp = data['rates']['GBP']
    chf = data['rates']['CHF']
    un_usd = ron / usd
    un_gbp = ron / gbp
    un_chf = ron / chf
   
