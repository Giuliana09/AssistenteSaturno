import pyttsx3
import pygame
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminhoAudio = os.path.join(BASE_DIR, 'audios')

pygame.init()
pygame.mixer.init()

def play_audio(audio):
    sons = os.path.join(os.path.join(caminhoAudio, audio))
    pygame.mixer.music.load(sons)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170) # número de palavras por minuto
    engine.setProperty('volume', 1) # min: 0, max: 1
    engine.say(audio)
    engine.runAndWait()