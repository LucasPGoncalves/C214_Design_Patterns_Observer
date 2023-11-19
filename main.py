from Observado import Aplicativo
from Observer import ObservadorPalavrasPadrao

if __name__ == "__main__":
    aplicativo = Aplicativo()
    observador = ObservadorPalavrasPadrao()
    aplicativo.adicionar_observador(observador)

    frase = input("Digite uma frase: ")
    aplicativo.notificar_observadores(frase)
