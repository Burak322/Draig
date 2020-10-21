import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
import psutil
import pyjokes
import pyautogui
from news import speak_news, getNewsUrl
from diction import translate
from loc import weather
from youtube import youtube
import psutil
import pyjokes
from sys import platform
import os
import getpass

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def screenshot():
    img = pyautogui.screenshot()
    img.save('kaydetmek istediğiniz dosya yolu/screenshot.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak("İşlemci kullanımı şuan "+usage)

    battery = psutil.sensors_battery()
    speak("batarya ")
    speak(battery.percent)


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Dinleniyor...')
        speak("Dinleniyor...")
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print("Algılanıyor...")
        speak("Algılanıyor...")
        query = r.recognize_google(audio, language='en-in')
        print(f'Kullanıcı dedi ki: {query}\n')
        speak(f'Kullanıcı dedi ki: {query}\n')

    except Exception as e:
        # print(e)

        print('Lütfen tekrar söyleyin...')
        speak('Lütfen tekrar söyleyin...')
        return 'None'
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Günaydın efendim")
        speak("Günaydın efendim")
    elif hour >= 12 and hour < 18:
        print("İyi öğleden sonları efendim")
        speak("İyi öğleden sonları efendim")

    else:
        speak('İyi akşamlar efendim')
        print("İyi akşamlar efendim")

    weather()
    speak('Ben Draig. Size nasıl yardımcı olabilirim efendim?')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak("İşlemci kullanımı "+usage)

    battery = psutil.sensors_battery()
    speak("batarya şuan")
    speak(battery.percent)


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def screenshot():
    img = pyautogui.screenshot()
    img.save('path of folder you want to save/screenshot.png')


if __name__ == '__main__':

    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome'

    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app'

    elif platform == "win32":
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    else:
        print('Unsupported OS')
        exit(1)

    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Vikipedide araştırılıyor...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'youtube downloader' in query:
            exec(open('youtube_downloader.py').read())

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Merhaba efendim. Sesimi değiştirdim nasıl olmuş?")

        if 'jarvis are you there' in query:
            speak("Evet efendim, komutlarınızı bekliyorum")

        elif 'open youtube' in query:

            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'play music' in query:
            os.startfile("D:\\RoiNa.mp3")

        elif 'search youtube' in query:
            speak('Youtube da ne araştırmamı istersiniz efendim?')
            youtube(takeCommand())
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'search' in query:
            speak('Ne araştırmamızı istiyorsunuz efendim?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Bulduğum sonuçlar bunlar' + search)

        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'your master' in query:
            if platform == "win32" or "darwin":
                speak('Beni By_Burak yarattı, Yaklaşık olarak 1 ayda.')
            elif platform == "linux" or platform == "linux2":
                name = getpass.getuser()
                speak(name, 'is my master. He is running me right now')

        elif 'your name' in query:
            speak('Adım Draig')
        elif 'stands for' in query:
            speak('Draig bir mitolojik bir varlığım. ')
        elif 'open code' in query:
            if platform == "win32":
                os.startfile(
                    "C:\\Users\\gs935\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('code .')

        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com/gauravsingh9356')

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'sleep' in query:
            sys.exit()

        elif 'dictionary' in query:
            speak('Sözlükte ne aramamı istersiniz')
            translate(takeCommand())

        elif 'news' in query:
            speak('tabiki efendim....')
            speak_news()
            speak('Bütün haberleri sunayımmı...')
            test = takeCommand()
            if 'yes' in test:
                speak('Tamamdır efendim, tarayıcı açılıyor..')
                webbrowser.open(getNewsUrl())
                speak('Bu internet sitesinden bütün haberleri okuyabilirsiniz')
            else:
                speak('Sorun değil')

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("Merhaba efendim, sesimi değiştirdim nasıl olmuş.")