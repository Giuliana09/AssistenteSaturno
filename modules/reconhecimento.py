import speech_recognition as sr
import os

#speak('Testando o sintetizador de voz da assistente')
def listen_microphone():
    microfone = sr.Recognizer()
    if not os.path.exists('recordings'):
        os.makedirs('recordings')

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=0.8)
        print("Ouvindo:")
        audio = microfone.listen(source)
        with open('recordings/speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("Você disse:", frase)
        return frase
    except sr.UnknownValueError:
        print("Não entendi")
        return ''
