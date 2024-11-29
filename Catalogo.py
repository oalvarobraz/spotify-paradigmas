from Musica import Musica
from api import reproduzir_musica_com_api_thread, tempo_em_segundos


class Catalogo:
    catalogo = []

    @staticmethod
    def get_catalogo():
        return Catalogo.catalogo

    @staticmethod
    def listar_musicas():
        if not Catalogo.catalogo:
            print("O catálogo está vazio.")
        else:
            print("\n=== Músicas disponíveis ===")
            for idx, musica in enumerate(Catalogo.catalogo):
                print(f"{idx + 1}. {musica.titulo} - {musica.artista} ({musica.duracao})")
            print("=============================")

    @staticmethod
    def adicionar_musica(musica: Musica):
        if musica not in Catalogo.catalogo:
            Catalogo.catalogo.append(musica)
            print(f"Música '{musica.titulo}' adicionada ao catálogo.")
        else:
            print(f"Música '{musica.titulo}' já está no catálogo.")

    @staticmethod
    def adicionar_musica_parametros(titulo, artista, duracao):
        musica = Musica(titulo, artista, duracao)
        if musica not in Catalogo.catalogo:
            Catalogo.catalogo.append(musica)
        else:
            print(f"Música '{musica.titulo}' já está no catálogo.")

    @staticmethod
    def reproduzir_musica(musica: Musica):
        if musica in Catalogo.catalogo:
            print(f"Tocando agora: {musica.titulo} - {musica.artista} ({musica.duracao})")
        else:
            print("Música não encontrada no catálogo.")

    @staticmethod
    def reproduzir_musica_api(musica: Musica):
        if musica in Catalogo.catalogo:
            reproduzir_musica_com_api_thread(musica.titulo, musica.artista)
        else:
            print("Música não encontrada no catálogo.")

    @staticmethod
    def buscar_musicas(criterio, valor):
        resultados = [musica for musica in Catalogo.get_catalogo() if
                      getattr(musica, criterio, "").lower() == valor.lower()]
        if resultados:
            print("Resultados encontrados:")
            for musica in resultados:
                print(f"{musica.titulo} - {musica.artista} ({musica.duracao})")

            resposta = input("Deseja tocar todas a(s) musica(s)? (Sim/Não)\n")
            if resposta.lower() in ['sim', 's', 'y', 'yes']:
                for musica in resultados:
                    Catalogo.reproduzir_musica_api(musica)
        else:
            print("Nenhuma música encontrada.")

    @staticmethod
    def buscar_musica(titulo, artista):
        for musica in Catalogo.get_catalogo():
            if musica.titulo.lower() == titulo.lower() and musica.artista.lower() == artista.lower():
                return musica
