import datetime
import pandas as pd

hora_atual = datetime.datetime.now()
hora_atual, minuto_atual = datetime.datetime.time(hora_atual).hour, datetime.datetime.time(hora_atual).minute
data_atual = datetime.datetime.date(datetime.datetime.today())


planilha_agenda = 'agenda.xlsx'
agenda = pd.read_excel(planilha_agenda)
print(agenda)

descricao, responsavel, hora_agenda = [], [], []

for index, row in agenda.iterrows():
    data = datetime.datetime.date(row['data'])
    hora_completa = datetime.datetime.strptime(str(row['hora']), '%H:%M:%S')
    hora = datetime.datetime.time(hora_completa).hour


    if data_atual == data:
        if hora >= hora_atual:
            descricao.append(row['descricao'])
            responsavel.append(row['responsavel'])
            hora_agenda.append(row['hora'])


def carrega_agenda():
    if descricao:
        return descricao, responsavel, hora_agenda
    else:
        return False




















