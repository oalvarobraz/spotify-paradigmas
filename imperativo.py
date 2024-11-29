from api import reproduzir_musica_com_api_thread, tempo_em_segundos
import threading
from queue import Queue
import time

queue = Queue()


catalago = [
    {'Titulo': 'Far Away', 'Artista': 'Nickelback', 'Duracao': '3:58', 'Id': 1},
    {'Titulo': 'Those Eyes', 'Artista': 'New West', 'Duracao': '3:41', 'Id': 2},
    {'Titulo': 'Control', 'Artista': 'Zoe Wees', 'Duracao': '3:51', 'Id': 3},
]

playlists = {}


def listar_musicas():
    print("\n=== Músicas disponíveis ===")
    for musica in catalago:
        print(f"{musica['Id']}. {musica['Titulo']} - {musica['Artista']} ({musica['Duracao']})")
    print("=============================")


def adicionar_musica(titulo, artista, duracao):
    """Adiciona uma nova música ao catálogo, garantindo IDs únicos."""
    for musica in catalago:
        if musica['Titulo'] == titulo and musica['Artista'] == artista:
            print(f"Música '{musica['Titulo']}' já está no catálogo.")
            return

    novo_id = buscar_maior_id(catalago) + 1
    catalago.append({'Titulo': titulo, 'Artista': artista, 'Duracao': duracao, 'Id': novo_id})
    print(f"Música '{titulo}' adicionada ao catálogo com ID {novo_id}.")


def reproduzir_musica(titulo, artista):
    for music in catalago:
        if music['Titulo'] == titulo and music['Artista'] == artista:
            print(f"Tocando agora: {music['Titulo']} - {music['Artista']} ({music['Duracao']})")
            return
    print("Música não encontrada!")


def criar_playlist(nome_playlist):
    if nome_playlist not in playlists:
        playlists[nome_playlist] = []
        print(f"Playlist '{nome_playlist}' criada.")
    else:
        print("Playlist já existe.")


def adicionar_musica_playlist(nome_playlist, titulo_musica, artista_musica):
    if nome_playlist not in playlists:
        print("Não existe uma playlist com esse nome")
        return
    for musica in playlists[nome_playlist]:
        if musica['Titulo'] == titulo_musica and musica['Artista'] == artista_musica:
            print("Música já está na playlist!")
            return
    for musica in catalago:
        if musica['Titulo'] == titulo_musica and musica['Artista'] == artista_musica:
            playlists[nome_playlist].append(musica)
            print(f"Música '{titulo_musica}' adicionada à playlist '{nome_playlist}'.")
            return
    print("Música não encontrada!")


def remover_musica_playlist(nome_playlist, titulo_musica, artista_musica):
    if nome_playlist not in playlists:
        print("Não existe uma playlist com esse nome.")
        return
    for musica in playlists[nome_playlist]:
        if musica['Titulo'] == titulo_musica and musica['Artista'] == artista_musica:
            playlists[nome_playlist].remove(musica)
            print(f"Música '{titulo_musica}' removida da playlist '{nome_playlist}'.")
            return
    print("Música não encontrada na playlist.")


def reproduzir_playlist(nome_playlist):
    if nome_playlist not in playlists:
        print("Playlist não encontrada")
        return
    if not playlists[nome_playlist]:
        print(f"A playlist '{nome_playlist}' está vazia.")
        return
    for musica in playlists[nome_playlist]:
        reproduzir_musica(musica['Titulo'], musica['Artista'])


def reproduzir_playlist_api(nome_playlist):
    if nome_playlist not in playlists:
        print("Playlist não encontrada")
        return
    if not playlists[nome_playlist]:
        print(f"A playlist '{nome_playlist}' está vazia.")
        return

    for musica in playlists[nome_playlist]:
        queue.put(musica)

    def tocar_da_fila():
        while not queue.empty():
            musica = queue.get()
            titulo = musica['Titulo']
            artista = musica['Artista']
            duracao = musica['Duracao']
            print(f"Tocando agora: {titulo} - {artista}")
            reproduzir_musica_com_api_thread(titulo, artista)

            tempo_duracao = tempo_em_segundos(duracao)
            print(f"Aguardando {tempo_duracao} segundos para a próxima música...")
            time.sleep(tempo_duracao)
            queue.task_done()

    threading.Thread(target=tocar_da_fila).start()


def mostrar_playlist(nome_playlist):
    if nome_playlist in playlists:
        print(f"Playlist: {nome_playlist}")
        for idx, musica in enumerate(playlists[nome_playlist]):
            print(f"{idx + 1}. {musica['Titulo']} - {musica['Artista']} ({musica['Duracao']})")
        if not len(playlists[nome_playlist]):
            print("Playlist está vázia")
    else:
        print("Playlist não encontrada.")


def buscar_musicas(criterio, valor):
    resultados = [musica for musica in catalago if valor.lower() in musica[criterio].lower()]
    if resultados:
        print("Resultados encontrados:")
        for musica in resultados:
            print(f"{musica['Titulo']} - {musica['Artista']} ({musica['Duracao']})")
    else:
        print("Nenhuma música encontrada com o critério especificado.")


def buscar_musica_por_id(id):
    for item in catalago:
        if item['Id'] == id:
            return item
    return None


def buscar_maior_id(catalogo):
    return max((musica['Id'] for musica in catalogo), default=0)


def buscar_musica_playlist(nome_playlist, criterio, valor):
    if nome_playlist not in playlists:
        print("Playlist não encontrada.")
        return
    resultados = [musica for musica in playlists[nome_playlist] if valor.lower() in musica[criterio].lower()]
    if resultados:
        print("Resultados encontrados:")
        for musica in resultados:
            print(f"{musica['Titulo']} - {musica['Artista']} ({musica['Duracao']})")

        resposta = input("Deseja todas a(s) musica(s)? (Sim/Não)\n")
        if resposta.lower() == 'sim' or resposta.lower() == 's' or resposta.lower() == 'y' or resposta.lower() == 'yes':
            for musica in resultados:
                reproduzir_musica_com_api_thread(musica['Titulo'], musica['Artista'])
    else:
        print("Nenhuma música encontrada.")


def listar_musicas_ordenadas():
    musicas_ordenadas = sorted(catalago, key=lambda x: x['Titulo'])
    print("\n=== Músicas em Ordem Alfabética ===")
    for idx, musica in enumerate(musicas_ordenadas):
        print(f"{musica['Id']}. {musica['Titulo']} - {musica['Artista']} ({musica['Duracao']})")
    print("===========================")


while True:
    print("\nMenu Principal:")
    print("1. Listar músicas no catálogo")
    print("2. Adicionar música ao catálogo")
    print("3. Criar playlist")
    print("4. Adicionar música a uma playlist")
    print("5. Remover música de uma playlist")
    print("6. Listar músicas em uma playlist")
    print("7. Reproduzir playlist")
    print("8. Buscar música no catálogo")
    print("9. Buscar música em uma playlist")
    print("10. Reproduzir uma música")
    print("11. Listar músicas no catálogo em ordem alfabética")
    print("12. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_musicas()
    elif opcao == "2":
        titulo = input("Título: ")
        artista = input("Artista: ")
        duracao = input("Duração: ")
        adicionar_musica(titulo, artista, duracao)
    elif opcao == "3":
        nome_playlist = input("Nome da playlist: ")
        if nome_playlist not in playlists:
            criar_playlist(nome_playlist)
        else:
            print("Playlist já existe.")
    elif opcao == "4":
        for idx, playlist in enumerate(playlists):
            print(f"{idx+1}. {playlist}")
        nome_playlist = input("Nome da playlist: ")
        listar_musicas()
        titulo_musica = input("Título da música: ")
        artista_musica = input("Artista da música: ")
        adicionar_musica_playlist(nome_playlist, titulo_musica, artista_musica)
    elif opcao == "5":
        for idx, playlist in enumerate(playlists):
            print(f"{idx + 1}. {playlist}")
        nome_playlist = input("Nome da playlist: ")
        listar_musicas()
        titulo_musica = input("Título da música: ")
        artista_musica = input("Artista da música: ")
        remover_musica_playlist(nome_playlist, titulo_musica, artista_musica)
    elif opcao == "6":
        for idx, playlist in enumerate(playlists):
            print(f"{idx + 1}. {playlist}")
        nome_playlist = input("Nome da playlist: ")
        mostrar_playlist(nome_playlist)
    elif opcao == "7":
        for idx, playlist in enumerate(playlists):
            print(f"{idx + 1}. {playlist}")
        nome_playlist = input("Nome da playlist: ")
        reproduzir_playlist_api(nome_playlist)
    elif opcao == "8":
        criterio = input("Critério de busca (Titulo/Artista): ").lower()
        valor = input(f"Valor de {criterio}: ")
        buscar_musicas(criterio, valor)
    elif opcao == "9":
        for idx, playlist in enumerate(playlists):
            print(f"{idx + 1}. {playlist}")
        nome_playlist = input("Nome da playlist: ")
        criterio = input("Critério de busca (Titulo/Artista): ").lower()
        valor = input(f"Valor de {criterio}: ")
        buscar_musica_playlist(nome_playlist, criterio, valor)
    elif opcao == "10":
        for idx, musica in enumerate(catalago):
            print(f"{musica['Id']}. {musica['Titulo']} - {musica['Artista']}")
        cod = int(input("Número da música: "))
        musica = buscar_musica_por_id(cod)
        if musica is not None:
            reproduzir_musica_com_api_thread(musica['Titulo'], musica['Artista'])
        else:
            print("Número não pertence ao catálogo. Tente novamente.")
    elif opcao == "11":
        listar_musicas_ordenadas()
    elif opcao == "12":
        print("Encerrando...")
        break
    else:
        print("Opção inválida. Tente novamente.")
