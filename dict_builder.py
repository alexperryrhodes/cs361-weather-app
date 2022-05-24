from weather_api import forecast_weather, historic_weather

def dict_builder(location, chart_type, time_type, data_type):
    
    if time_type == 'Historic':
        weather = historic_weather(location)
        city_name = weather[0]['location']['name']
        region_name = weather[0]['location']['region']
    
    else:
        weather = forecast_weather(location)
        city_name = weather['location']['name']
        region_name = weather['location']['region']

    if data_type == 'Temperature':
        data = 'temp_f'
    else:
        data = 'precip_in'

    dict_data = {
        'graph_type': chart_type
        ,'graph_height': 500
        ,'graph_width': 700
        ,'x_axis': []
        ,'y_axis': []
        ,'export_type': 'png'
        ,'export_location': 'static/weather_chart'
        ,'graph_title':f'{time_type} {data_type} in {city_name}, {region_name}'
        ,'x_axis_label': 'Date'
        ,'y_axis_label': f'{data_type}'
    }

    if time_type == 'Historic':
        for date_index in range(3,0, -1):
            for hour_index in range(0, 24):
                    datetime = weather[date_index]['forecast']['forecastday'][0]['hour'][hour_index]['time']
                    date_point = weather[date_index]['forecast']['forecastday'][0]['hour'][hour_index][data]

                    dict_data['x_axis'].append(datetime)
                    dict_data['y_axis'].append(date_point)
    else:
        for date_index in range(1,3):
            for hour_index in range(0, 24):
                datetime = weather['forecast']['forecastday'][date_index]['hour'][hour_index]['time']
                date_point = weather['forecast']['forecastday'][date_index]['hour'][hour_index][data]

                dict_data['x_axis'].append(datetime)
                dict_data['y_axis'].append(date_point)

    return dict_data
