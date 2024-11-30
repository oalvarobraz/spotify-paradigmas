from Musica import Musica
from Playlist import Playlist
from Catalogo import Catalogo


catalogo = Catalogo()

musica1 = Musica("Bohemian Rhapsody", "Queen", "5:54", 1)
musica2 = Musica("Imagine", "John Lennon", "3:03", 2)
musica3 = Musica("Hotel California", "Eagles", "6:31", 3)
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
        print("10. Reproduzir uma música pelo ID")
        print("11. Listar músicas no catálogo em ordem alfabética")
        print("12. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            catalogo.listar_musicas()

        elif opcao == "2":
            titulo = input("Título: ")
            artista = input("Artista: ")
            duracao = input("Duração: ")
            musica = Musica(titulo, artista, duracao, -1)
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
            if nome_playlist:
                catalogo.listar_musicas()
                try:
                    id_musica = int(input("Digite o ID da música: "))
                    musica = catalogo.buscar_musica_por_id(id_musica)
                    if musica:
                        playlists[nome_playlist].adicionar_musica(musica)
                        print(f"Música '{musica.titulo}' adicionada com sucesso!")
                    else:
                        print("ID inválido. Música não encontrada.")
                except ValueError:
                    print("Entrada inválida. Digite apenas o ID da música.")

        elif opcao == "5":
            nome_playlist = selecionar_playlist()
            if nome_playlist:
                playlists[nome_playlist].listar_musicas()
                try:
                    id_musica = int(input("Digite o ID da música para remover: "))
                    musica = catalogo.buscar_musica_por_id(id_musica)
                    if musica:
                        playlists[nome_playlist].remover_musica(musica)
                        print(f"Música '{musica.titulo}' removida com sucesso!")
                    else:
                        print("ID inválido. Música não encontrada.")
                except ValueError:
                    print("Entrada inválida. Digite apenas o ID da música.")

        elif opcao == "6":
            nome_playlist = selecionar_playlist()
            if nome_playlist:
                playlists[nome_playlist].listar_musicas()

        elif opcao == "7":
            nome_playlist = selecionar_playlist()
            if nome_playlist:
                playlists[nome_playlist].reproduzir_api()

        elif opcao == "8":
            criterio = input("Buscar por (titulo/artista): ").lower()
            valor = input(f"Digite o {criterio}: ")
            catalogo.buscar_musicas(criterio, valor)

        elif opcao == "9":
            nome_playlist = selecionar_playlist()
            if nome_playlist:
                criterio = input("Buscar por (titulo/artista): ").lower()
                valor = input(f"Digite o {criterio}: ")
                playlists[nome_playlist].buscar_musicas(criterio, valor)

        elif opcao == "10":
            try:
                catalogo.listar_musicas()
                id_musica = int(input("Digite o ID da música: "))
                musica = catalogo.buscar_musica_por_id(id_musica)
                if musica:
                    catalogo.reproduzir_musica_api(musica)
                else:
                    print("ID inválido. Música não encontrada.")
            except ValueError:
                print("Entrada inválida. Digite apenas o ID da música.")

        elif opcao == "11":
            musicas_ordenadas = sorted(catalogo.get_catalogo(), key=lambda x: x.titulo)
            print("\n=== Músicas em Ordem Alfabética ===")
            for musica in musicas_ordenadas:
                print(f"{musica.cod}. {musica.titulo} - {musica.artista} ({musica.duracao})")

        elif opcao == "12":
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
