from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from timezonefinder import TimezoneFinder
import datetime
import requests
import json
import pytz
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re
import random, os

path = r"C:\weatherforecasting\pics"

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)
#root.config(bg="#fff")


def getWeather():

    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=1ffa0adf78dbd80be223db699a66d5f3"

        json_data = requests.get(api).json()

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°C"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid city Entry")

def window2():
    try:

        city_name =textfield.get()


        root1 = Toplevel(root)
        root.iconify()
        root1.title("Weather App/more information")
        root1.geometry("1250x550")


        #root1.resizable(True, True)
        # getting the city's coordinates (lat and lon)

        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=1ffa0adf78dbd80be223db699a66d5f3"

        req = requests.get(url)
        data = req.json()
        name = data['name']
        lon = data['coord']['lon']
        lat = data['coord']['lat']
        con = data['weather'][0]['main']
        des = data['weather'][0]['description']
        tem = int(data['main']['temp'] - 273.15)
        pres = data['main']['pressure']
        humi = data['main']['humidity']
        wind = data['wind']['speed']

        print(name, lon, lat)

        exclude = "minute,hourly"

        url2 = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid=1ffa0adf78dbd80be223db699a66d5f3'

        req2 = requests.get(url2)
        data2 = req2.json()
        days = []
        nights = []
        descr = []

        for i in data2['daily']:
            days.append(round(i['temp']['day'] - 273.15, 2))

            nights.append(round(i['temp']['night'] - 273.15, 2))

            descr.append(i['weather'][0]['main'] + ": " + i['weather'][0]['description'])

        string = f'{name}-8daysforecast]\n'

        dates = f'{name}-8daysforecast\n'

        # Let's now loop for as much days as there available (8 in this case):
        for i in range(len(days)):

        # We want to print out the day (day1,2,3,4..)
        # Also, day 1 = today and day 2 = tomorrow for reference

            if i == 0:
                string += f'\nDay{i + 1}(Today)\n'
                dates += f'\nDay{i + 1}(Today)\n'

            elif i == 1:
                string += f'\nDay{i + 1}(Tomorrow)\n'
                dates += f'\nDay{i + 1}(Tomorrow)\n'


            else:
                string += f'\nDay{i + 1}\n'
                dates += f'\nDay{i + 1}\n'

            string += 'Morning:' + str(days[i]) + '°C' + "\n"
            string += 'Night:' + str(nights[i]) + '°C' + "\n"
            string += 'Conditions:' + descr[i] + '\n'

        print(string)

        # da = re.findall("[\cccd]", dates)
        # print(da)

        l = list()
        dd = datetime.date.today()
        d1 = r'{}'.format(datetime.date.today())
        print(d1)
        l.append(d1)
        d2 = r'{}'.format(dd + datetime.timedelta(days=1))
        l.append(d2)
        print(d2)
        d3 = r'{}'.format(dd + datetime.timedelta(days=2))
        d4 = r'{}'.format(dd + datetime.timedelta(days=3))
        d5 = r'{}'.format(dd + datetime.timedelta(days=4))
        d6 = r'{}'.format(dd + datetime.timedelta(days=5))
        d7 = r'{}'.format(dd + datetime.timedelta(days=6))
        d8 = r'{}'.format(dd + datetime.timedelta(days=7))
        l.append(d3)
        l.append(d4)
        l.append(d5)
        l.append(d6)
        l.append(d7)
        l.append(d8)
        print(l)


        print(days)
        print(nights)
        # print(descr)
        def zoom():
            root1.destroy()
            root.deiconify()
        back_image = PhotoImage(file="back.png")
        im = Button(root1, image=back_image, command=zoom)
        im.place(x=20, y=20)

        label1 = Label(root1, text="CITY      :", font=("Helvetica", 15, "bold"), fg="black")
        label1.place(x=20, y=80)
        c = Label(root1, text=name, font=("arial", 10))
        c.place(x=130, y=85)

        label2 = Label(root1, text="LATITUDE   :", font=("Helvetica", 15, "bold"), fg="black")
        label2.place(x=20, y=110)
        la = Label(root1, text=lat, font=("arial", 10))
        la.place(x=160, y=115)

        label3 = Label(root1, text="LONGITUDE :", font=("Helvetica", 15, "bold"), fg="black")
        label3.place(x=20, y=140)
        lo = Label(root1 , text=lon, font=("arial", 10))
        lo.place(x=160, y=145)

        label4 = Label(root1, text="Temperature :", font=("Helvetica", 15, "bold"), fg="black")
        label4.place(x=20, y=170)
        t = Label(root1, text=(tem, "°C"), font=("arial", 10))
        t.place(x=160, y=175)

        label5 = Label(root1, text="Condition :", font=("Helvetica", 15, "bold"), fg="black")
        label5.place(x=20, y=200)
        c = Label(root1, text=(con, "|", "FEELS", "LIKE", tem, "°C"), font=("arial", 8))
        c.place(x=130, y=205)

        label6 = Label(root1, text="WIND        :", font=("Helvetica", 15, "bold"), fg="black")
        label6.place(x=20, y=230)
        w = Label(root1, text=wind, font=("arial", 10))
        w.place(x=150, y=235)

        label7 = Label(root1, text="HUMIDITY   :", font=("Helvetica", 15, "bold"), fg="black")
        label7.place(x=20, y=260)
        h = Label(root1, text=humi, font=("arial", 10))
        h.place(x=150, y=270)

        label8 = Label(root1, text="DESCRIPTION :", font=("Helvetica", 15,'bold'), fg="black")
        label8.place(x=20, y=290)
        d = Label(root1, text=des, font=("arial", 10))
        d.place(x=170, y=295)

        label9 = Label(root1, text="PRESSURE  :", font=("Helvetica", 15, 'bold'), fg="black")
        label9.place(x=20, y=320)
        pr = Label(root1, text=pres, font=("arial", 10))
        pr.place(x=160, y=325)


        #graph
        fig = Figure(figsize=(9, 5))
        a = fig.add_subplot(111)
        a.plot(l, nights, label="nights in °C")
        a.plot(l, days, label="mornings in °C")
        a.set_xlabel('days')
        a.set_ylabel('temperatue in °C')
        a.set_title(f'temperatures graph on {name} in °C')
        a.legend()
        a.grid()

        canv = FigureCanvasTkAgg(fig, master=root1)
        canv.draw()

        get_widz = canv.get_tk_widget()
        get_widz.place(x=290, y=20)

        root1.mainloop()

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid city Entry")



# search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

info = PhotoImage(file="infor.png")
imageinfo = Button(root, image=info, cursor="hand2", command=window2)
imageinfo.place(x=700, y=40)

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# logo
logo_image = PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=150)

# Bottom box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=("arial", 15, 'bold'))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# label
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()