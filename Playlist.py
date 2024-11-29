from Musica import Musica
from api import tempo_em_segundos, reproduzir_musica_com_api_thread
from Catalogo import Catalogo
import time


class Playlist:
    def __init__(self, nome: str, musicas: list[Musica]):
        self._nome = nome
        self._musicas = []
        for musica in musicas:
            if musica in Catalogo.get_catalogo():
                self._musicas.append(musica)
            else:
                print(f"Música {musica.titulo} - {musica.artista} não está no catálogo.")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._nome = valor
        else:
            raise ValueError("O nome da playlist deve ser uma string não vazia.")

    @property
    def musicas(self):
        return self._musicas

    @musicas.setter
    def musicas(self, lista_musicas):
        if all(isinstance(m, Musica) for m in lista_musicas):
            self._musicas = lista_musicas
        else:
            raise ValueError("Todos os itens na lista devem ser instâncias da classe 'Musica'.")

    def adicionar_musica(self, musica: Musica):
        if musica in self.musicas:
            print("Música já está na playlist!")
        elif musica in Catalogo.get_catalogo():
            self.musicas.append(musica)
        else:
            print("Música não está no catálogo!")

    def remover_musica(self, musica: Musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
        else:
            print("Música não encontrada na playlist.")

    def listar_musicas(self):
        if not self.musicas:
            print("A playlist está vazia.")
        else:
            print(f"Playlist: {self.nome}")
            for idx, musica in enumerate(self.musicas):
                print(f"{idx + 1}. {musica.titulo} - {musica.artista} ({musica.duracao})")

    def reproduzir(self):
        if not self.musicas:
            print("Playlist está vazia!")
        else:
            for music in self.musicas:
                print(f"Tocando agora: {music.titulo} - {music.artista} ({music.duracao})")

    def reproduzir_api(self):
        if not self.musicas:
            print("Playlist está vazia!")
        else:
            for music in self.musicas:
                reproduzir_musica_com_api_thread(music.titulo, music.artista)
                tempo_duracao = tempo_em_segundos(music.duracao)
                print(f"Aguardando {tempo_duracao} segundos para a próxima música...")
                time.sleep(tempo_duracao)

    def buscar_musicas(self, criterio, valor):
        if criterio not in ['titulo', 'artista', 'duracao']:
            print("Critério inválido. Use 'titulo', 'artista' ou 'duracao'.")
            return
        resultados = []
        for musica in self.musicas:
            if getattr(musica, criterio).lower() == valor.lower():
                resultados.append(musica)
        if resultados:
            print("Resultados encontrados:")
            for musica in resultados:
                print(f"{musica.titulo} - {musica.artista} ({musica.duracao})")

            resposta = input("Deseja todas a(s) musica(s)? (Sim/Não)\n")
            if resposta.lower() in ['sim', 's', 'y', 'yes']:
                for musica in resultados:
                    Catalogo.reproduzir_musica_api(musica)
        else:
            print("Nenhuma música encontrada.")
