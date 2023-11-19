from abc import ABC, abstractmethod

class ObservadorPalavras(ABC):
    @abstractmethod
    def notificar(self, frase):
        pass

class ObservadorPalavrasPadrao(ObservadorPalavras):
    def notificar(self, frase):
        palavras = frase.split()
        total_palavras = len(palavras)
        palavras_pares_caracteres = [palavra for palavra in palavras if len(palavra) % 2 == 0]
        palavras_maiusculas = [palavra for palavra in palavras if palavra[0].isupper()]

        print("Total de palavras:", total_palavras)
        print("Palavras com quantidade par de caracteres:", len(palavras_pares_caracteres))
        print("Palavras começadas com maiúsculas:", len(palavras_maiusculas))

class Aplicativo:
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        if isinstance(observador, ObservadorPalavras):
            self.observadores.append(observador)
        else:
            raise ValueError("O observador deve ser uma instância de ObservadorPalavras")

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, frase):
        for observador in self.observadores:
            observador.notificar(frase)

if __name__ == "__main__":
    aplicativo = Aplicativo()
    observador = ObservadorPalavrasPadrao()
    aplicativo.adicionar_observador(observador)

    frase = input("Digite uma frase: ")
    aplicativo.notificar_observadores(frase)