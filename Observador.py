from ObserverInterface import observadorInterface

class ObservadorPalavrasPadrao(observadorInterface):
    def __init__(self) -> None:
        self.total_palavras = 0
        self.palavras_pares_caracteres = 0
        self.palavras_maiusculas = 0

    def notificar(self, frase):
        palavras = frase.split()
        self.total_palavras = len(palavras)
        self.palavras_pares_caracteres = [palavra for palavra in palavras if len(palavra) % 2 == 0]
        self.palavras_maiusculas = [palavra for palavra in palavras if palavra[0].isupper()]

        print("Total de palavras:", self.total_palavras)
        print("Palavras com quantidade par de caracteres:", len(self.palavras_pares_caracteres))
        print("Palavras começadas com maiúsculas:", len(self.palavras_maiusculas))