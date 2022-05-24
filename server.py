from flask import Flask, render_template, request, make_response, redirect, flash
from weather_api import current_weather, forecast_weather, historic_weather
from dict_builder import dict_builder
from chart_builder import chart_builder
from datetime import datetime
import time


app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/", methods=(['GET','POST']))
def login(): 
    if request.method == 'POST':
        userID = request.form.get("username")
        userPW = request.form.get("password")
        print(userID)
        print(userPW)
        with open("login/loginUser.txt", "w") as logger:
            logger.write(userID + " " + userPW) 

        time.sleep(2)
        with open("login/validUserResponse.txt") as responder:
            reply = responder.read()
            print('Reply:', reply)

        if 'Validated' in reply:
            return redirect('/weather')
        
        elif 'Invalid' in reply:
            flash('Incorrect Password, Please Try Again!')
            return redirect('/')
        
        else:
            return redirect('/')

    else:
        return render_template('index.html')


@app.route("/weather", methods=('GET', 'POST'))
def home():
    
    zip = request.form.get("zip", default=None)
    chart_type = request.form.get("chart-type", default='line')
    time_type = request.form.get("time-type", default='Historic')
    data_type = request.form.get("data-type", default='Temperature')

    if zip is None:
        zip = request.cookies.get("zip", default=None)
        if zip is None:
            zip = "97331"

    curr_weather = current_weather(zip)
    hist_weather = historic_weather(zip)
    fore_weather = forecast_weather(zip)
    
    weather_json = dict_builder(zip, chart_type, time_type, data_type)

    chart_builder(weather_json)

    res = make_response(render_template('weather.html', curr_data = curr_weather, hist_data = hist_weather, fore_weather = fore_weather))
    res.set_cookie('zip', zip)
    return res

@app.context_processor
def utility_processor():
    def format_date(str_date):
        formatdate = datetime.strptime(str_date, '%Y-%m-%d')
        day_of_week = formatdate.strftime('%A')
        return day_of_week
    return dict(format_date=format_date)

