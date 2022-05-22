import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import pyaudio
import wave
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("my name intellio. Please tell me how may I help you")
def takeCommand(ask=False):
    r = sr.Recognizer()
    if ask:
        speak(ask)
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

 
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'stop' in query:
            speak('kill switch initiated')
            break



        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[66])) 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f" the time is {strTime}")
        elif 'search' in query:
            search = takeCommand('what do you want to search?')
            url = 'www.google.com/search?q=' + search
            webbrowser.open_new(url)
            speak('the results of the search of ' + search)
        elif 'do you know my name' in query:
            speak('i would love to know your name')
            x = takeCommand('what is your name ?')
            speak('hi ' + x)
        elif 'open youtube' in query:
            speak('..here..')
            x = 'www.youtube.com'
            webbrowser.open_new(x)
        elif 'open stackoverflow' in query:
            speak('..here..')
            x = 'www.stackoverflow.com'
            webbrowser.open_new(x)
        elif'hello' in query:
            speak('hello')
        elif 'bye' in query:
            speak('thank you. for your time') 
            break
        elif 'hai' in query:
            speak('hello') 
        elif 'open website 1' in query:
            x = 'https://vealize.my.to/'
            webbrowser.open_new(x)
        elif 'thank you' in query:
            speak('your welcome')
            speak('if you are done. please say stop or bye. i will get disabled myself')
        elif 'record my audio' in query:
            speak('please speak the audio you want to record')
            speak('Press CTRL+C to quit')
            audio = pyaudio.PyAudio()
            stream = audio.open(format=pyaudio.paInt16,channels=1, rate=44100, input=True,frames_per_buffer=1024)
            frames = []
            try:
                while True:
                    data = stream.read(1024)
                    frames.append(data)
            except KeyboardInterrupt:
                pass
            stream.stop_stream()
            stream.close()
            audio.terminate()

            Sound_file = wave.open('Recorded audio.wav',mode='wb')
            Sound_file.setnchannels(1)
            Sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            Sound_file.setframerate(44100)
            Sound_file.writeframes(b''.join(frames))
            Sound_file.close() 
        elif 'generate a random number' in query:
            o = speak('Enter the below requirements')
            speak(o)
            x = int(input('Enter the lower limit '))
            y = int(input('Enter the upper limit '))
            number = random.randint(x, y)
            speak('your number is generated below')
            print('Random number generated is ', number)
        elif 'feeling lucky' in query:
            p = 'https://www.google.com/doodles'
            webbrowser.open_new_tab(p)
        elif 'anime' in query:
            e = 'https://animixplay.to/'
            webbrowser.open_new_tab(e)
        elif 'translate' in query:
            i = 'https://www.bing.com/search?q=translate&cvid=51aa33b1827e47fa95114e8a6b3f54ec&aqs=edge.0.0l9.2318j0j1&pglt=299&FORM=ANNTA1&PC=U531'
            webbrowser.open_new_tab(i)
        
            webbrowser.open_new_tab(d)
        elif 'who is your creator' in query:
            speak("the supreme conqueror. D-pit")
        elif 'open mail' in query:
            l = 'https://mail.google.com/mail/u/0/#inbox'
            webbrowser.open(l)
            speak('your mails')
