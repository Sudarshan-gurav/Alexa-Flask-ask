# Alexa-Flask-ask

Install flask-ask
command : 

      pip install flask-ask

- you need python 3.6

- if facing problem we need to downgrade pip 9.0.3
      
      pip install pip==9.0.3 --user
      pip install flask_ask --user
      pip install --upgrade pip  --user 

- After that install flask-ask 

      pip install cryptography==2.1.4 --user 

Create account in developer portal of amezon create our custom skill link:- https://developer.amazon.com 

- custom skill name :- Hi (anything) 

- Invocation : hi (weak up word)

intent name :
       
       NameIntent
       YesNoIntent
       StuProfntIntent
       PrefessionIntent
       CityIntent
       WeatherIntent
       WeatherReplyIntent

Utterances:

NameIntent: 

      i am {name}
      my name is {name}
      {name} here
      {name}

ConfirmNameIntent:
      
      {name } here
      i am {name}
      my name is {name}
      {name}

StuProfntIntent
      
      i am {stage}
      {stage}

ProfessionalIntent
      
      {prof}
      i am {prof}

CityIntent:
      
      {city}
      i am from {city}

WeatherIntent:
      
      it's {weather} here
      it's {weather} today
      it's {weather} 
      {weather}
  
WeatherReplyIntent
      
      haha
      really
      thank you
      nice
  
YesNoIntent:
      
     {response}

stageslot

      responseslot
      profslot
      weatherslot
      AMAZON.GB_FIRST_NAME
      AMAZON.US_CITY

Download ngrox link : https://ngrok.com/download

