from partido import Partido

class Deputado:
    def __init__(self, nome='', partido=Partido(), numero=0, indicadorDeCorrupcao=0):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.indicadorDeCorrupcao = indicadorDeCorrupcao
    def __str__(self):
        return f" {self.nome} - {self.numero} / Avaliação: {self.indicadorDeCorrupcao} -> Partido: {self.partido}"
