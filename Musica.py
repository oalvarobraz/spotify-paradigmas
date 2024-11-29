from api import reproduzir_musica_com_api, tempo_em_segundos


class Musica:
    def __init__(self, titulo: str, artista: str, duracao: str):
        self._titulo = titulo
        self._artista = artista
        self._duracao = duracao

    # Getter e Setter para 'titulo'
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def artista(self):
        return self._artista

    @artista.setter
    def artista(self, value):
        self._artista = value

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, value):
        self._duracao = value

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracao})"

