import requests
from bs4 import BeautifulSoup as BS
import datetime
import json

#export headers to server
headers = {'User-Agent':'MMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#URL for parser
url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
#connection to URL
full_page = requests.get(url)
# print(full_page) #connection check

# Cooking a Beautiful Soup, preparing data for manipulations
soup = BS(full_page.content, 'html.parser')
# print(soup) #self check

#main cycle, asking user which city we want to check weather in

def main():
    print('Weather report in Estonian cities')
    while True:
        user_choice = input('1.Weather in Narva\n2.Weather in Tallinn-Harku\n0.Exit\n>>')
        if user_choice == '1':
            parser(user_choice) #export user choice to function parser()
        elif user_choice == '2':
            parser(user_choice)
        elif user_choice == '0':
            break
        else:
            print('Choice is out of range!')

### end of function

#parser function looks for requested data according to user choice
def parser(user_choice):
    if user_choice == '1':
        test_td = soup.find('td', text='Narva') #find table line where first cell is Narva
        sb = test_td.find_next_siblings()  #find all next siblings
        city = 'Narva' #export name of the city to use in user output
        output(sb, city) #export siblings of line called Narva to function output() to show results
    elif user_choice == '2':
        test_td = soup.find('td', text='Tallinn-Harku')
        sb = test_td.find_next_siblings()
        city = 'Tallinn-Harku'
        output(sb, city)

### end of function

#function output shows results to user

def output(sb, city):
    #first cell in line has name of city, next contains weahter parameters, as indexed below:
    print(f'Current weather in {city}')
    print(f'Air temp. mean, C: {sb[0].text}')
    print(f'Air temp. max, C: {sb[1].text}')
    print(f'Air temp. min, C: {sb[2].text}')
    print(f'Soil temp. min, C: {sb[3].text}')
    print(f'Temp. 2cm above soil, C: {sb[4].text}')
    print(f'Mean relative humidity: {sb[5].text}%')
    print(f'Min. relative humidity: {sb[6].text}%')
    print(f'Mean wind speed, m/s: {sb[7].text}')
    print(f'Max. wind speed, m/s: {sb[8].text}')
    print(f'Mean perciptation, mm: {sb[9].text}')
    print(f'Visible sun time, hours: {sb[10].text}')
    print(f'End of weather report for {city} at {datetime.datetime.now()}') #adding timestamp
    print()

    #prepare data for dump into JSON
    report = {
        "city": {
            "name": city,
            "report_time": str(datetime.datetime.now()),
            "mean_air_temp": sb[0].text,
            "max_air_temp": sb[1].text,
            "min_air_temp": sb[2].text,
            "min_soil_temp": sb[3].text,
            "2cm_above_soil_temp": sb[4].text,
            "mean_rel_humidity": sb[5].text,
            "min_rel_humidity": sb[6].text,
            "mean_wind_speed": sb[7].text,
            "min_wind_speed": sb[8].text,
            "mean_perciptation_mm": sb[9].text,
            "visible_sun_hours": sb[10].text
                    }
    }
    # dump data into JSON file
    with open('weather_report.json', 'w') as file:
        json.dump(report, file, indent=2)

### end of function

# start main cycle

main()

# end of code
