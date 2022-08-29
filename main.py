import json

import requests
from datetime import date, timedelta, datetime
import pandas as pd

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def calculate_max_min_temp(dataset):
    try:
        print(type(dataset))
        all_max_temps=[]
        all_min_temps = []
        all_avg_humidity = []
        all_total_rainfall_mm=[]
        for data in dataset:
            # print(data['forecast']['forecastday'][0]['day']['maxtemp_c'])
            all_max_temps.append(data['maxtemp_c'])
            all_min_temps.append(data['mintemp_c'])
            all_avg_humidity.append(data['avghumidity'])
            all_total_rainfall_mm.append(data['totalprecip_mm'])

        return {'max':max(all_max_temps),'min':min(all_min_temps),'humidity': sum(all_avg_humidity)/len(all_avg_humidity),'rainfall':sum(all_total_rainfall_mm)/len(all_total_rainfall_mm)}

    except Exception as e:
        print(e)



def print_hi():
    districts={
        'Barguna':'Barguna'
    }
    start_date = date(2010, 1, 1)
    end_date = date(2010, 12, 31)
    responses=[]
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    dates= pd.date_range("2010-01-01","2010-12-31",freq='d').strftime("%Y-%m-%d")
    print(len(dates))
    for single_date in dates:
        print(single_date)
        # barguna_response = requests.get("http://api.weatherapi.com/v1/history.json?key=cdea9d77fffa443d95d71526222908&q=22.15788500,90.11440790&dt="+single_date,headers=headers)
        response = requests.get("http://api.weatherapi.com/v1/history.json?key=cdea9d77fffa443d95d71526222908&q=22.6406,90.1987&dt=" + single_date,headers=headers)
        responses.append(response.json()['forecast']['forecastday'][0]['day'])

    # print(responses)
    max_temp=calculate_max_min_temp(responses)
    print(max_temp)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

