import pyttsx3
import re


engine = pyttsx3.init('nsss')

def speak(content):
    engine.say(content)
    engine.runAndWait()

def speakLimited(content):
    engine.say(trimContent(content))
    engine.runAndWait()

def getnline(str, n):
    return ". ".join(str.split(".")[:n])

def trimContent(content):
    res = len(re.findall(r'\w+', content))
    sentences = re.split(r'[.!?]+', content)
    sencount = len(sentences)
    while (res > 150):
        sentences.pop()
        tmp = ". ".join(sentences)
        res = len(re.findall(r'\w+', tmp))
    content = ". ".join(sentences)
    return content
