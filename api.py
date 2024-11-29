import spotipy
from spotipy.oauth2 import SpotifyOAuth
from threading import Thread
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope=os.getenv("SPOTIPY_SCOPE")
))


def listar_dispositivos():
    dispositivos = sp.devices()
    if dispositivos['devices']:
        print("Dispositivos disponíveis:")
        for dispositivo in dispositivos['devices']:
            print(f"Nome: {dispositivo['name']}, Tipo: {dispositivo['type']}, ID: {dispositivo['id']}")
    else:
        print("Nenhum dispositivo ativo encontrado. Abra o Spotify em algum dispositivo e tente novamente.")


def tocar_musica(nome_musica, artista):
    dispositivos = sp.devices()
    if not dispositivos['devices']:
        print("Nenhum dispositivo ativo encontrado. Abra o Spotify em algum dispositivo e tente novamente.")
        return

    dispositivo_id = dispositivos['devices'][0]['id']

    resultados = sp.search(q=f"track:{nome_musica} artist:{artista}", type="track", limit=1)
    if resultados['tracks']['items']:
        track_uri = resultados['tracks']['items'][0]['uri']
        sp.start_playback(device_id=dispositivo_id, uris=[track_uri])
        print(f"Tocando: {nome_musica} - {artista}")
    else:
        print("Música não encontrada.")


def reproduzir_musica_com_api(titulo, artista):
    print(f"Tentando reproduzir: {titulo} - {artista} via Spotify...")
    tocar_musica(titulo, artista)


def reproduzir_musica_com_api_thread(titulo, artista):
    def task():
        reproduzir_musica_com_api(titulo, artista)

    thread = Thread(target=task)
    thread.start()


def tempo_em_segundos(duracao):
    minutos, segundos = map(int, duracao.split(':'))
    return minutos * 60 + segundos
