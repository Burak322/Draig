import geocoder
import requests
import json
import pyttsx3

g = geocoder.ip('me')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def weather():
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        speak(str(data_json['coord']['lat']) + 'latitude' + str(data_json['coord']['lon']) + 'longitude')
        speak('Şuanki konum ' + data_json['name'] + data_json['sys']['country'] + 'dia')
        speak('hava ' + weather_desc['main'])
        speak('Rüzgar hızı ' + str(wind['speed']) + ' metre per second')
        speak('Sıcaklık: ' + str(main['temp']) + 'degree celcius')
        speak('Nem ' + str(main['humidity']))


if __name__ == '__main__':
    weather()
