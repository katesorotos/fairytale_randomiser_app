# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:16:43 2019

@author: Kate Sorotos
"""

from flask import Flask, render_template
from random import randint
import requests
app = Flask(__name__)


@app.route("/")
def index():
    message = "This is an app to pracice using API's - It will randomly generate a new fairytale each time you refresh the page."

    gender = ["girl", "boy"]
    random_gender = randint(0, len(gender) - 1)
    gender = gender[random_gender]
    
    if gender == 'girl':
        pronoun = 'she'
        pronoun_1 = 'She'
        pronoun_2 = 'her'
        pronoun_3 = 'Her'
        pronoun_4 = 'her'
    else:
        pronoun = 'he'
        pronoun_1 = 'He'
        pronoun_2 = 'his'
        pronoun_3 = 'His'
        pronoun_4 = 'him'

    endpoint = requests.get("https://randomuser.me/api/")
    name_info = endpoint.json()
    first = name_info['results'][0]['name']['first'].title()
    last = name_info['results'][0]['name']['last'].title()
    place = name_info['results'][0]['location']['city'].title()

    weather = ["clear", "hot", "sunny", "rainy", "windy", "snowy", "stormy", "cloudy"]
    random_weather = randint(0, len(weather) - 1)
    weather = weather[random_weather]

    activity = requests.get("http://www.boredapi.com/api/activity/")
    bored_data = activity.json()
    generated_activity = bored_data['activity'].lower()

    magical_person = ["fairy godmother", "psychic", "palmist", "magical cat"]
    random_magical_person = randint(0, len(magical_person) - 1)
    magical_person = magical_person[random_magical_person]

    advice = requests.get("http://api.adviceslip.com/advice")
    advice_data = advice.json()
    random_advice = advice_data['slip']['advice']

    animal = ['pig', 'donkey', 'monkey', 'frog', 'bird']
    random_animal = randint(0, len(animal) - 1)
    animal = animal[random_animal]

    transport = ['flying carpet', 'broomstick', 'DeLorean', 'flying motobike', 'hover car']
    random_transport = randint(0, len(animal) - 1)
    transport = transport[random_transport]

    return render_template("index.html", title="Home", **locals())


if __name__ == "__main__":
    app.run(debug=True)
