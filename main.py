from Musica import Musica
from Playlist import Playlist
from Catalogo import Catalogo


catalogo = Catalogo()

musica1 = Musica("Bohemian Rhapsody", "Queen", "5:54")
musica2 = Musica("Imagine", "John Lennon", "3:03")
musica3 = Musica("Hotel California", "Eagles", "6:31")
catalogo.adicionar_musica(musica1)
catalogo.adicionar_musica(musica2)
catalogo.adicionar_musica(musica3)

playlists = {}


def listar_playlists():
    if not playlists:
        print("Nenhuma playlist criada ainda.")
    else:
        print("\n=== Playlists Disponíveis ===")
        for idx, nome in enumerate(playlists):
            print(f"{idx+1}. {nome}")
        print("=============================")


def selecionar_playlist():
    listar_playlists()
    try:
        numero_playlist = int(input("Digite o número da playlist: ")) - 1
        nomes_playlists = list(playlists.keys())
        if 0 <= numero_playlist < len(nomes_playlists):
            return nomes_playlists[numero_playlist]
        else:
            print("Número inválido. Tente novamente.")
            return None
    except ValueError:
        print("Entrada inválida. Digite apenas o número da playlist.")
        return None


def menu():
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
            catalogo.listar_musicas()
        elif opcao == "2":
            titulo = input("Título: ")
            artista = input("Artista: ")
            duracao = input("Duração: ")
            musica = Musica(titulo, artista, duracao)
            catalogo.adicionar_musica(musica)
        elif opcao == "3":
            nome = input("Nome da playlist: ")
            if nome in playlists:
                print("Playlist já existe.")
            else:
                playlists[nome] = Playlist(nome, [])
                print(f"Playlist '{nome}' criada.")
        elif opcao == "4":
            nome_playlist = selecionar_playlist()
            if nome_playlist in playlists:
                print("\n========================")
                catalogo.listar_musicas()
                print("========================\n")
                try:
                    numero_musica = int(input("Digite o número da música: ")) - 1
                    musicas_catalogo = catalogo.get_catalogo()
                    if 0 <= numero_musica < len(musicas_catalogo):
                        musica = musicas_catalogo[numero_musica]
                        playlists[nome_playlist].adicionar_musica(musica)
                        print(f"Música '{musica.titulo}' adicionada com sucesso!")
                    else:
                        print("Número inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite apenas o número da música.")
            else:
                print("Playlist não encontrada.")
        elif opcao == "5":
            nome_playlist = selecionar_playlist()
            if nome_playlist in playlists:
                playlists[nome_playlist].listar_musicas()
                try:
                    numero_musica = int(input("Digite o número da música para remover: ")) - 1
                    musicas_playlist = playlists[nome_playlist].musicas
                    if 0 <= numero_musica < len(musicas_playlist):
                        musica = musicas_playlist[numero_musica]
                        playlists[nome_playlist].remover_musica(musica)
                        print(f"Música '{musica.titulo}' removida com sucesso!")
                    else:
                        print("Número inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite apenas o número da música.")
            else:
                print("Playlist não encontrada.")
        elif opcao == "6":
            nome_playlist = selecionar_playlist()
            if nome_playlist in playlists:
                playlists[nome_playlist].listar_musicas()
            else:
                print("Playlist não encontrada.")
        elif opcao == "7":
            nome_playlist = selecionar_playlist()
            if nome_playlist in playlists:
                playlists[nome_playlist].reproduzir_api()
            else:
                print("Playlist não encontrada.")
        elif opcao == "8":
            criterio = input("Buscar por (titulo/artista): ").lower()
            valor = input(f"Digite o {criterio}: ")
            catalogo.buscar_musicas(criterio, valor)
        elif opcao == "9":
            nome_playlist = selecionar_playlist()
            if nome_playlist in playlists:
                criterio = input("Buscar por (titulo/artista): ").lower()
                valor = input(f"Digite o {criterio}: ")
                playlists[nome_playlist].buscar_musicas(criterio, valor)
            else:
                print("Playlist não encontrada.")
        elif opcao == "10":
            catalogo.listar_musicas()
            titulo = input("Título da música: ")
            artista = input("Artista da música: ")
            m = catalogo.buscar_musica(titulo, artista)
            catalogo.reproduzir_musica_api(m)
        elif opcao == "11":
            musicas_ordenadas = sorted(catalogo.get_catalogo(), key=lambda x: x.titulo)
            print("\n=== Músicas em Ordem Alfabética ===")
            for idx, musica in enumerate(musicas_ordenadas):
                print(f"{idx + 1}. {musica.titulo} - {musica.artista} ({musica.duracao})")
        elif opcao == "12":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
