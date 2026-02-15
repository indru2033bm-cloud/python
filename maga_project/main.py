import speech_recognition as sr  
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speck(text):
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    speck("Initializing Jarivis......")
    while True:
        #listen for the word "Jarivis"
        #obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
    
# recc ognize speech using sphinx
        try:
            command = r.recognize_sphinx(audio)
            print(command)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        if "Jarivis" in command:
            speck("Yes, how can I help you?")
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
            try:
                command = r.recognize_sphinx(audio)
                print(command)
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))
            if "open YouTube" in command:
                webbrowser.open("https://www.youtube.com")
                speck("Opening YouTube")