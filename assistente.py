import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")  # Ignora todos os avisos
import pyttsx3
#import tensorflow as ts
import librosa
import matplotlib.pyplot as plt
import seaborn as sns
import pyaudio
import webbrowser as wb
import speech_recognition as sr
from playsound import playsound
import random
import os
import pygame

import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt
sns.set()



import datetime

pygame.init()
pygame.mixer.init()


# exibir hora e data

hora = datetime.datetime.now().strftime('%H:%M')
#print (hora)
#pyttsx3.speak(hora)
date = datetime.date.today().strftime('%d/%B/%Y')
#print(data)
date = date.split('/')
#print(data)

#pyttsx3.speak(data[1])
def play_audio(audio):
    sons = os.path.join('audios', audio)
    pygame.mixer.music.load(sons)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


from modules import comandos_respostas
comandos = comandos_respostas.comandos
respostas = comandos_respostas.respostas

#print(comandos)
#print(respostas)

meu_nome = 'Saturno'

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

def search(frase):
    wb.get(chrome_path).open('https://www.google.com/search?q=' + frase)

#search('aprendizagem de máquina')



def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120) # número de palavras por minuto
    engine.setProperty('volume', 1) # min: 0, max: 1
    engine.say(audio)
    engine.runAndWait()

#speak('Testando o sintetizador de voz da assistente')
def listen_microphone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=0.8)
        print('Ouvindo:')
        audio = microfone.listen(source)
        with open('recordings/speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print('Você disse: ' + frase)
    except sr.UnknownValueError:
        frase = ''
        print('Não entendi')
    return frase




playing = False
mode_control = False
print('[INFO] Pronto para começar!')
play_audio('n1.mp3')

while (1):
    result = listen_microphone()

    if meu_nome in result:
        result = str(result.split(meu_nome + ' ')[1])
        result = result.lower()
        print('Acionou a assistente!')
        # print('Após o processamento: ', result)

        if result in comandos[0]:
            play_audio('n2.mp3')
            speak('Até agora minhas funções são: ' + respostas[0])


        if result in comandos[1]:
            play_audio('n2.mp3')
            speak('Pode falar!')
            result = listen_microphone()
            anotacao = open('anotacao.txt', mode='a+', encoding='utf-8')
            anotacao.write(result + '\n')
            anotacao.close()
            speak(''.join(random.sample(respostas[1], k=1)))
            speak('Deseja que eu leia os lembretes?')
            result = listen_microphone()
            if result == 'sim' or result == 'pode ler':
                with open('anotacao.txt') as file_source:
                    lines = file_source.readlines()
                    for line in lines:
                        speak(line)
            else:
                speak('Ok!')

        if result in comandos[2]:
            play_audio('n2.mp3')
            speak(''.join(random.sample(respostas[2], k=1)))
            result = listen_microphone()
            search(result)

        if result in comandos[3]:
            play_audio('n2.mp3')
            speak('Agora são ' + datetime.datetime.now().strftime('%H:%M'))

        if result in comandos[4]:
            play_audio('n2.mp3')
            speak('Hoje é dia ' + date[0] + ' de ' + date[1])

        if result == 'encerrar':
            play_audio('n2.mp3')
            speak(''.join(random.sample(respostas[4], k=1)))
            break
    else:
        play_audio('n3.mp3')


