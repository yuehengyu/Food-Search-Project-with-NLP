import speech_recognition as sr
from os import path

def speechtotest(pathname):
    AUDIO_FILE = path.join(path.dirname(path.realpath('G:/djiango/directlyStudy/output.wav')), pathname)
    r = sr.Recognizer()
    with sr.WavFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
    IBM_USERNAME = "03fcb5b3-13c0-4d9d-820c-909a0bc2b29c"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = "F0M0fXlOFtTJ"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
    try:
        return r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))

