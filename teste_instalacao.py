

import pygame
import os

pygame.init()
pygame.mixer.init()

def play_audio(nome_arquivo):
    caminho = os.path.join('audios', nome_arquivo)
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

play_audio('n2.mp3')
play_audio('n1.mp3')
play_audio('n3.mp3')

# pip install charset_normalizer, chardet

#import speech_recognition
#print('Speech Recognition: ', speech_recognition.__version__)

#import pyttsx3
#pyttsx3.speak('Testando a biblioteca')

#import tensorflow
#print('TensorFlow: ', tensorflow.__version__)

#import librosa
#print('Librosa:', librosa.__version__)

#import matplotlib
#print('Matplotlib: ', matplotlib._get_version())

#import seaborn
#print('Seaborn: ', seaborn.__version__)

#import pyaudio
#print('Pyaudio ok!')

#----------------------------------------------------
# exibir hora e data

hora = datetime.datetime.now().strftime('%H:%M')
#print (hora)
#pyttsx3.speak(hora)
date = datetime.date.today().strftime('%d/%B/%Y')
#print(data)
date = date.split('/')
#print(data)



# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows

# Linux
# chrome_path = '/usr/bin/google-chrome %s'


