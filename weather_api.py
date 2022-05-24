import requests
import json
from datetime import datetime, timedelta, date


def url_builder(type, date_url, location):

    url = 'http://api.weatherapi.com/v1/' + type + '?key=' + '2436f386044444adac815931221804' + '&q=' + location + date_url

    return url

def current_weather(location):

    url = url_builder('current.json', "", location)

    response = requests.get(url)
    response_text = response.text
    data = json.loads(response_text)

    return data


def historic_weather(location):
    output = []
    start_date = datetime.today().date()
    for day in range(1,5):

        date = start_date - timedelta(days=day)
        str_date = "&dt=" + str(date)

        url = url_builder('history.json', str_date, location)

        data = json.loads(requests.get(url).text)

        output.append(data)

    return output

def forecast_weather(location):
    url = url_builder('forecast.json', '&days=3', location)
    data = json.loads(requests.get(url).text)

    return data