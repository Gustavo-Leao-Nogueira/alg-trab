class Partido:
    def __init__(self, sigla='', numero=0):
        self.sigla = sigla
        self.numero = numero
    def __str__(self):
        return f"[ Sigla: {self.sigla}, Numero: {self.numero} ]"

