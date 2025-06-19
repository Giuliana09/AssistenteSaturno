import requests
import tempfile
import pygame
import webbrowser as wb
import threading

def search(frase):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    wb.get(chrome_path).open('https://www.google.com/search?q=' + frase)


def buscar_jamendo(termo):
    if not termo:
        return None

    termo = str(termo).lower()
    ID = "59beb811"
    url = "https://api.jamendo.com/v3.0/tracks"
    params = {
        "client_id": ID,
        "format": "json",
        "limit": 1,
        "audioformat": "mp31",
        "order": "popularity_total",
    }

    # Lista de gêneros comuns da Jamendo
    generos = [
        "rock", "pop", "jazz", "blues", "hiphop", "rap", "classical",
        "country", "electronic", "reggae", "metal", "funk", "samba",
        "forro", "pagode", "sertanejo", "trap", "mpb", "gospel", "indie"
    ]

    termo_tratado = termo.lower()

    if termo_tratado in generos:
        params["tags"] = termo_tratado  # Busca por gênero
    else:
        params["namesearch"] = termo_tratado

    resp = requests.get(url, params=params)

    if resp.status_code == 200:
        dados = resp.json()
        if dados["results"]:
            return dados["results"][0]["audio"]

    return None

def tocar_jamendoThread(url_audio):
    def tocar():
        with requests.get(url_audio, stream=True) as r:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                ride = f.name
        pygame.mixer.music.load(ride)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    thread = threading.Thread(target=tocar, daemon=True)
    thread.start()