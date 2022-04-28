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
x = ''
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
    root.after(50000, getNews)
    global xurl
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()
    ron = data['rates']['RON']
    usd = data['rates']['USD']
    gbp = data['rates']['GBP']
    chf = data['rates']['CHF']
    un_usd = ((ron / usd)*(1/100))+(ron / usd)
    un_gbp = ((ron / gbp)*(1/100))+(ron / gbp)
    un_chf = ((ron / chf)*(1/100))+(ron / chf)
    leu = (ron*(1/100))+ron

    un_euro_lbl = Label(root,text='Euro: '+str('{:.2f}'.format(leu)),font =('Arial',14,'bold'))
    un_euro_lbl.place(x=890,y=5)
    un_usd_lbl = Label(root, text='USD : ' + str('{:.2f}'.format(un_usd)), font=('Arial', 14, 'bold'))
    un_usd_lbl.place(x=890,y=30)
    un_gbp_lbl = Label(root, text='GBP: ' + str('{:.2f}'.format(un_gbp)), font=('Arial', 14, 'bold'))
    un_gbp_lbl.place(x=890, y=55)
    un_chf_lbl = Label(root, text='CHF:  ' + str('{:.2f}'.format(un_chf)), font=('Arial', 14, 'bold'))
    un_chf_lbl.place(x=890, y=80)

    api_key = "http://api.openweathermap.org/data/2.5/weather?lat=44&lon=28&appid=89bb00f7b33659800dc33d0af3c9fbb1"
    json_data = requests.get(api_key).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)

    api_key = "75c69d67d407464ebbb4fac15d97d9a6"
    url = "https://newsapi.org/v2/top-headlines?country=ro&apiKey="+api_key
    news = requests.get(url).json()
    final_info = "Constanta: "  + " " + str(temp) + '\xb0C - '+ condition
    label1.config(text=final_info)

    articles = news['articles']
    my_articles = []
    my_news = ""
    my_urls.clear()
    xurl= ''

    for article in articles:
        my_urls.append(article['url'])
        my_articles.append(article['title'])

    for i in range(15):
        my_news = my_news + str(i+1)+". " + my_articles[i] + '\n''\n'

    label.config(text = my_news)
    time = datetime.datetime.now()
    time_label = Label(root, text=time.strftime("%Y-%m-%d %H:%M"),font =('Arial',14,'bold'))
    time_label.place(x=3,y=3)

    # send SMS
    # if time.hour == 12 and time.minute == 00:
    #     print('53 min')
    #     account_sid = 'xxxxxxxxxxxxx'
    #     auth_token = 'xxxxxxxxxxxxxxx'
    #     client = Client(account_sid, auth_token)
    #
    #     message = client.messages.create(
    #         messaging_service_sid='MG8bc5f4c385b7ea7db8b9ce2b166910e0',
    #         body=f'\nEuro: {euro_sms}\n USD: {usd_sms}\n  Constanta: {temp}\xb0C',
    #         to='+40730xxxxxxx')
    #     print(message.sid)

def getWeather():
    global counter
    global pic
    if counter <1:

        bg_color = "#1ec9b8"
        top = Toplevel()
        top.geometry('290x450')
        top.resizable(width=False, height=False)
        top.title('Weather info')
        top.config(bg=bg_color)
        top.iconbitmap('sun.ico')

        time1 = datetime.datetime.now()

        # day/night
        images = ["sun.png", 'moon.png']
        if time1.hour > 20:
            pic = PhotoImage(file=images[1])
        if time1.hour < 5:
            pic = PhotoImage(file=images[1])
        else:
            pic = PhotoImage(file=images[0])

        sun_lbl = Label(top, image=pic, bg=bg_color)
        sun_lbl.place(x=210, y=35)

        def getRefresh():

            global final_info_label
            global label1
            global condition
            global x
            global label5
            conditions.clear()

            api_key = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=89bb00f7b33659800dc33d0af3c9fbb1"
            json_data = requests.get(api_key).json()
            condition = json_data['weather'][0]['main']
            temp = int(json_data['main']['temp'] - 273.15)
            min_temp = int(json_data['main']['temp_min'] - 273.15)
            max_temp = int(json_data['main']['temp_max'] - 273.15)
            feels_like = int(json_data['main']['feels_like'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            # sea_level = float(json_data['main']['sea_level']/1000)
            wind_speed = int(json_data['wind']['speed'] * 3.6)
            sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 7200))
            sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] + 7200))

            final_info = oras + " " + str(temp) + '\xb0C - ' + condition
            final_data1 = 'Max Temp: ' + str(max_temp) + '\xb0C' '\n' + 'Min Temp: ' + str(min_temp) + '\xb0C' + \
                          '\n' + 'Temp feels like: ' + str(feels_like) + '\xb0C''\n' + 'Sunrise: ' + str(
                sunrise) + ' am' + '\n' \
                          + 'Sunset: ' + str(sunset) + ' pm''\n' + 'Presure: ' + str(
                pressure) + 'mmHg''\n' + 'Humidity: ' + str(humidity) + '%' '\n' \
                          + 'Wind Speed: ' + str(wind_speed) + 'km/h''\n' ''  # + 'Sea level: ' + str(sea_level)+'m'

            conditions.append(condition)

            images1 = ["nori.png", 'moon.png', 'rain.png', 'soare.png', 'snow.png', 'canicula.png', 'fulgere.png',
                       'luna nori.png', 'nori soare.png', 'temp scazute.png']
            if conditions[0] == 'Clouds':
                x = PhotoImage(file=images1[0])
                icon_lbl = Label(top, image=x, bg=bg_color)
                icon_lbl.place(x=80, y=110)
            if conditions[0] == 'Clear' and time1.hour > 20:
                x = PhotoImage(file=images1[1])
                icon_lbl = Label(top, image=x, bg=bg_color)
                icon_lbl.place(x=80, y=110)
            if conditions[0] == 'Clear' and time1.hour < 20:
                x = PhotoImage(file=images1[3])
                icon_lbl = Label(top, image=x, bg=bg_color)
                icon_lbl.place(x=80, y=110)
            if conditions[0] == 'Snow':
                x = PhotoImage(file=images1[4])
                icon_lbl = Label(top, image=x, bg=bg_color)
                icon_lbl.place(x=80, y=110)
            if conditions[0] == 'Rain':
                x = PhotoImage(file=images1[2])
                icon_lbl = Label(top, image=x, bg=bg_color)
                icon_lbl.place(x=80, y=105)

            time_label = Label(top, text=time1.strftime("%Y-%m-%d %H:%M"), font=('Arial', 18, 'bold'), bg=bg_color)
            time_label.place(x=10, y=50)
            final_info_label = tk.Label(top, text=final_info, font=('Arial', 18, 'bold'), bg=bg_color, justify='left')
            final_info_label.place(x=10, y=80)
            label5 = tk.Label(top, text=final_data1, font=('Arial', 18, 'bold'), bg=bg_color, justify='left')
            label5.place(x=10, y=200)

        counter +=1

        # icon_lbl = Label(top, image=x, bg=bg_color)
        # icon_lbl.place(x=80, y=110)

        button_weather = tk.Button(top, font=('Arial', 16, 'bold'), text='Weather details', activebackground='green',
                                   fg='green', command=lambda: [getRefresh()])
        button_weather.place(x=5, y=5)

    def select_city(event):
        # global final_info_label
        final_info_label.destroy()
        label5.destroy()
        global lat
        global lon
        global oras

        if my_Combo.get() == 'Constanta':
            oras = "Constanta"
            lat, lon = constanta
        if my_Combo.get() == 'Brasov':
            oras = "Brasov"
            lat, lon = brasov
        if my_Combo.get() == 'Timisoara':
            oras = "Timisoara"
            lat, lon = timisoara
        if my_Combo.get() == 'Bucuresti':
            oras = "Bucuresti"
            lat, lon = bucuresti
        if my_Combo.get() == 'Cluj':
            oras = "Cluj"
            lat, lon = cluj
        if my_Combo.get() == 'Oradea':
            oras = "Oradea"
            lat, lon = oradea
        if my_Combo.get() == 'Sibiu':
            oras = "Sibiu"
            lat, lon = sibiu
        if my_Combo.get() == 'Select City':
            final_info_label.destroy()
            label5.destroy()

    options = [
        "Select City",
        "Brasov",
        "Bucuresti",
        "Cluj",
        "Constanta",
        "Oradea",
        "Sibiu",
        "Timisoara"]

    clicked = StringVar()
    clicked.set(options[0])

    my_Combo = ttk.Combobox(top, value=options, width=10)
    my_Combo.current(0)
    my_Combo.bind("<<ComboboxSelected>>", select_city)
    my_Combo.place(x=200, y=10)

    button_weather = tk.Button(top, font=('Arial', 16, 'bold'), text='Weather details', activebackground='green',
                               fg='green', command=lambda: [getRefresh()])
    button_weather.place(x=5, y=5)
    getRefresh()

    def Counter():
        global counter
        counter = False
        top.destroy()
        
    top.protocol("WM_DELETE_WINDOW", Counter)

class ButtonX():

    def __init__(self,a,b,c):
        self.button_open = tk.Button(root, font=('Elephant',8,'italic'),fg='red', text='Open', command=lambda: self.openSite(c))
        self.button_open.place(x=a, y=b)

    def openSite(self,c):
        webbrowser.open_new(my_urls[c])

ButtonX(1,109,0)
ButtonX(1,147,1)
ButtonX(1,185,2)
ButtonX(1,223,3)
ButtonX(1,261,4)
ButtonX(1,299,5)
ButtonX(1,337,6)
ButtonX(1,375,7)
ButtonX(1,413,8)
ButtonX(1,451,9)
ButtonX(1,489,10)
ButtonX(1,527,11)
ButtonX(1,565,12)
ButtonX(1,603,13)
ButtonX(1,641,14)

news1 = tk.Label(root, font=('deutsch gothic',60), text="Daily News ")
news1.place(x=10,y=25)
button = tk.Button(root, font = ('Arial',16,'bold'), text='Refresh News',activebackground='green',fg='green', command = getNews)
button.place(x=420, y=8)
button_weather = tk.Button(root, font = ('Arial',16,'bold'), text='Weather details',activebackground='green',fg='green', command = (getWeather))
button_weather.place(x=410, y=60)
label = tk.Label(root, font =('Arial',12,'bold'), justify='left')
label.place(x=50, y=110)

label1 = tk.Label(root, font =('Arial',14,'bold'))
label1.place(x=180, y=3)
label2 = tk.Label(root, font =('Arial',12,'bold'), justify='left',height=6)
label2.place(x=620, y=1)
label3 = tk.Label(root, font =('Arial',12,'bold'), justify='left',height=6)
label3.place(x=820, y=1)

getNews()

root.mainloop()
