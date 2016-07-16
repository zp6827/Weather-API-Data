import requests
from pprint import pprint
import datetime

# Use zip code 30083
# not including my api id for obvious reasons
user_apiid = ''
current_date = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()


def main():
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=30083,us&APPID=" + user_apiid + "&units=imperial")
    # print(r.status_code)

    wformat = r.json()
    # pprint(wformat)
    # print('\n')

    print('{:25} {}'.format('Name:', wformat['name']))
    print('{:25} {} {}'.format('Current Temperature:', wformat['main']['temp'], 'degrees fahrenheit'))
    print('{:25} {} {}'.format('Atmospheric Pressure:', wformat['main']['pressure'], 'hPa'))
    print('{:25} {} {}'.format('Wind Speed:', wformat['wind']['speed'], 'mph'))
    print('{:25} {}'.format('Wind Direction:', wformat['wind']['deg']))
    print('{:25} {} {}'.format('Time of Report:', current_date, current_time))

if __name__ == '__main__':
    main()