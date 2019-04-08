
import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session 

##------------------------ library--------


app = Flask(__name__)

ask = Ask(app, "/")  

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

#----- launch -------------

@ask.launch
def start_intro():
    welcome_msg = render_template('A1')    
    return question(welcome_msg)   # alexa response

@ask.intent("NameIntent") # user response
def intro_round(name):
    try:
        round_msg = render_template('A2',name=name)
        session.attributes['name'] = name 
        return question(round_msg) # alexa response
    except:
        return question("Can you please repeat one more I am getting")

@ask.session_ended
def session_ended():
    return "{}", 200

@ask.intent("YesNoIntent")
def yes_no(response):
    if response == "no":
        repeat = render_template('NoA')
    else:
        name = session.attributes['name']    
        repeat = render_template('YesA',name=name)

    return statement(repeat)


@ask.intent("StuProfntIntent")
def stud_prof(stage):
    if stage == "student":
        profe = render_template('StudA')
    else:
        profe = render_template('ProfA')
    return statement(profe)

@ask.intent("PrefessionIntent")
def prof(prof):
    res = ''
    if prof == " ":
        return statement('Good')
    else:
        res = render_template('A4',prof=prof)
        re_prompt = render_template('A5')
        return statement(res).reprompt(re_prompt)

@ask.intent("CityIntent")
def City_fun(city):
    session.attributes['city'] = city
    nice = render_template('A6',city=city)
    return statement(nice)

@ask.intent("WeatherIntent")
def weather_fun(weather):
    print('--------',weather)
    try:
        if weather == "sunny":
            ret_weather = render_template("A7Sunny")
        elif weather == "cloudy":
            ret_weather = render_template("A8Cloudy")
        elif weather == "rainy":
            ret_weather = render_template("A9Rainy")
        elif weather == "windy":
            ret_weather = render_template("A10Windy")
        elif weather == "snowy":
            ret_weather = render_template("A11Snowy")
    except:
        return question("Invalid weather")
    return statement(ret_weather)

@ask.intent("WeatherReplyIntent")
def weather_reply():
    name = session.attributes['name'] 
    reply = render_template("A12",name=name)
    return statement(reply)
if __name__ == '__main__':
    app.run(debug=True)
