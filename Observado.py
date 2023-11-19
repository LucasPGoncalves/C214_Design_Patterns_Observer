from ObserverInterface import observadorInterface

class Aplicativo:
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        if isinstance(observador, observadorInterface):
            self.observadores.append(observador)
        else:
            raise ValueError("O observador deve ser uma instância de ObservadorPalavras")

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, frase):
        for observador in self.observadores:
            observador.notificar(frase)