from ObserverInterface import observadorInterface

class ObservadorPalavrasPadrao(observadorInterface):
    def notificar(self, frase):
        palavras = frase.split()
        total_palavras = len(palavras)
        palavras_pares_caracteres = [palavra for palavra in palavras if len(palavra) % 2 == 0]
        palavras_maiusculas = [palavra for palavra in palavras if palavra[0].isupper()]

        print("Total de palavras:", total_palavras)
        print("Palavras com quantidade par de caracteres:", len(palavras_pares_caracteres))
        print("Palavras começadas com maiúsculas:", len(palavras_maiusculas))