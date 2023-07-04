import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import re

city_name = "hyderabad"

#getting the city's coordinates (lat and lon)
url ="https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=1ffa0adf78dbd80be223db699a66d5f3"

#print(url)

# parse the Json
req = requests.get(url)
data = req.json()

# get the name, the longitude and latitude
name = data['name']
lon = data['coord']['lon']
lat = data['coord']['lat']

print(name, lon, lat)

exclude = "minute,hourly"

url2 = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid=1ffa0adf78dbd80be223db699a66d5f3'
#print(url2)

# Let's now parse the JSON
req2 = requests.get(url2)
data2 = req2.json()
#print(data2)

# Let's now get the temp for the day, the night and the weather conditions
days = []
nights = []
descr = []

# We need to access 'daily'
for i in data2['daily']:
    # We notice that the temperature is in Kelvin, so we need to do -273.15 for every datapoint

    # Let's start by days
    # Let's round the decimal numbers to 2
    days.append(round(i['temp']['day'] - 273.15, 2))

    # Nights
    nights.append(round(i['temp']['night'] - 273.15, 2))

    # Let's now get the weather condition and the description
    # 'weather' [0] 'main' + 'weather' [0] 'description'
    descr.append(i['weather'][0]['main'] + ": " + i['weather'][0]['description'])

#print(days)
#print(nights)
#print(descr)

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


l = list()
dd=datetime.date.today()
d1 = r'{}'.format(datetime.date.today())
print(d1)
l.append(d1)
d2 = r'{}'.format(dd+datetime.timedelta(days=1))
l.append(d2)
print(d2)
d3 = r'{}'.format(dd+datetime.timedelta(days=2))
d4 = r'{}'.format(dd+datetime.timedelta(days=3))
d5 = r'{}'.format(dd+datetime.timedelta(days=4))
d6 = r'{}'.format(dd+datetime.timedelta(days=5))
d7 = r'{}'.format(dd+datetime.timedelta(days=6))
d8 = r'{}'.format(dd+datetime.timedelta(days=7))
l.append(d3)
l.append(d4)
l.append(d5)
l.append(d6)
l.append(d7)
l.append(d8)
print(l)


"""
l.append(d1)
print(l)
for i in range(8):
    i=d1+datetime.timedelta(days=i)
    l.append(i)

print(l)
"""

