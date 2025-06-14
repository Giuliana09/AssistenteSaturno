from comandos_respostas import comandos, respostas
from audio import play_audio, speak
from reconhecimento import listen_microphone
from acoes import pesquisar, buscar_jamendo, tocar_jamendoThread
from util import hora_atual, data_hoje
import pygame
import warnings
import seaborn as sns
import random
with warnings.catch_warnings():
    warnings.simplefilter("ignore")  # Ignora todos os avisos

sns.set()


meu_nome = 'Saturno'
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


        elif result in comandos[1]:
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

        elif result in comandos[2]:
            play_audio('n2.mp3')
            speak(''.join(random.sample(respostas[2], k=1)))
            result = listen_microphone()
            pesquisar(result)

        elif result in comandos[3]:
            play_audio('n2.mp3')
            speak('Agora são ' + hora_atual())

        elif result in comandos[4]:
            play_audio('n2.mp3')
            speak('Hoje é dia ' + data_hoje())

        elif result in comandos[5]:
            play_audio('n2.mp3')
            speak(''.join(random.sample(respostas[5], k=1)))

        elif "tocar" in result:
            nome = result.replace("tocar", "").strip()
            play_audio('n2.mp3')
            speak(f"Tocando {nome}")
            link = buscar_jamendo(nome)
            if link:
                tocar_jamendoThread(link)
            else:
                speak("Não encontrei essa música.")

        elif result in ['pausar', 'pause']:
            pygame.mixer.music.pause()
            speak("Música pausada.")

        elif result in ['continuar', 'retomar']:
            pygame.mixer.music.unpause()
            speak("Continuando a música.")

        elif result in ['parar música', 'parar']:
            pygame.mixer.music.stop()
            speak("Música parada.")

        elif result == 'encerrar':
            play_audio('n2.mp3')
            speak(''.join(random.sample(respostas[4], k=1)))
            break
    else:
        play_audio('n3.mp3')
