import datetime

def hora_atual():
    return datetime.datetime.now().strftime('%H:%M')

def data_hoje():
    hoje = datetime.datetime.now()
    dia = hoje.strftime('%d')
    mes = hoje.strftime('%B')
    ano = hoje.strftime('%Y')
    meses_pt = {
        'January': 'janeiro', 'February': 'fevereiro', 'March': 'março',
        'April': 'abril', 'May': 'maio', 'June': 'junho',
        'July': 'julho', 'August': 'agosto', 'September': 'setembro',
        'October': 'outubro', 'November': 'novembro', 'December': 'dezembro'
    }
    return f"{dia} de {meses_pt[mes]} de {ano}"
