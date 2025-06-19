from modules.comandos_respostas import comandos, respostas
from modules.audio import play_audio, speak
from modules.reconhecimento import listen_microphone
from modules.acoes import search, buscar_jamendo, tocar_jamendoThread
from modules.util import hora_atual, data_hoje
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




def iniciar_assistente(atualizar_status, atualizar_fala_usuario, atualizar_resposta, verificar_rodando):
    print("Assistente iniciado!")
    while verificar_rodando():
        atualizar_status("Ouvindo...")
        result = listen_microphone()
        atualizar_fala_usuario(result)

        if meu_nome in result:
            result = str(result.split(meu_nome + ' ')[1])
            result = result.lower()
            atualizar_status("Processando...")
            print('Acionou a assistente!')


            if result in comandos[0]:
                play_audio('n2.mp3')
                resposta = 'Até agora minhas funções são: ' + respostas[0]
                atualizar_resposta(resposta)
                speak(resposta)


            elif result in comandos[1]:
                play_audio('n2.mp3')
                anotar = 'Pode falar!'
                atualizar_resposta(anotar)
                speak(anotar)
                result = listen_microphone()
                anotacao = open('anotacao.txt', mode='a+', encoding='utf-8')
                anotacao.write(result + '\n')
                anotacao.close()
                resposta = ''.join(random.sample(respostas[1], k=1))
                atualizar_resposta(resposta)
                speak(resposta)
                pergunta = 'Deseja que eu leia os lembretes?'
                atualizar_resposta(pergunta)
                speak(pergunta)
                result = listen_microphone()
                if result == 'sim' or result == 'pode ler':
                    with open('anotacao.txt') as file_source:
                        lines = file_source.readlines()
                        for line in lines:
                            speak(line)
                            atualizar_resposta(line)

                else:
                    speak('Ok!')

            elif result in comandos[2]:
                play_audio('n2.mp3')
                pesquisa= ''.join(random.sample(respostas[2], k=1))
                atualizar_resposta(pesquisa)
                speak(pesquisa)

                atualizar_status("Ouvindo o que pesquisar...")
                termo_pesquisa = listen_microphone()
                atualizar_fala_usuario(termo_pesquisa)

                search(termo_pesquisa)
                resposta = f"Aqui está o que encontrei sobre {termo_pesquisa}."
                atualizar_resposta(resposta)
                speak(resposta)


            elif result in comandos[3]:
                play_audio('n2.mp3')
                resposta = 'Agora são ' + hora_atual()
                atualizar_resposta(resposta)
                speak(resposta)

            elif result in comandos[4]:
                play_audio('n2.mp3')
                resposta = 'Hoje é dia ' + data_hoje()
                atualizar_resposta(resposta)
                speak(resposta)

            elif result in comandos[5]:
                play_audio('n2.mp3')
                resposta = ''.join(random.sample(respostas[5], k=1))
                atualizar_resposta(resposta)
                speak(resposta)

            elif "tocar" in result:
                nome = result.replace("tocar","").strip()
                play_audio('n2.mp3')
                resposta = f"Tocando {nome}"
                atualizar_resposta(resposta)
                speak(resposta)
                link = buscar_jamendo(nome)
                if link:
                    tocar_jamendoThread(link)
                else:
                    resposta= "Não encontrei essa música."
                    atualizar_resposta(resposta)
                    speak(resposta)

            elif result in ['pausar', 'pause', 'pausa']:
                pygame.mixer.music.pause()
                resposta = "Música pausada."
                atualizar_resposta(resposta)
                speak(resposta)

            elif result in ['continuar', 'retomar']:
                pygame.mixer.music.unpause()
                resposta = "Continuando a música."
                atualizar_resposta(resposta)
                speak(resposta)

            elif result in ['parar música', 'parar', 'para']:
                pygame.mixer.music.stop()
                resposta ="Música parada."
                atualizar_resposta(resposta)
                speak(resposta)

            elif result == 'encerrar':
                play_audio('n2.mp3')
                resposta = ''.join(random.sample(respostas[4], k=1))
                atualizar_resposta(resposta)
                speak(resposta)
                break
        else:
            play_audio('n3.mp3')

    atualizar_status("Pausado")