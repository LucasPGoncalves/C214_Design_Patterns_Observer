import unittest
from Observado import Aplicativo
from Observador import ObservadorPalavrasPadrao

class ObserverTest(unittest.TestCase):
    def test_adicionarObservador(self):
        aplicativo = Aplicativo()
        observador = ObservadorPalavrasPadrao()
        aplicativo.adicionar_observador(observador)

        self.assertEqual(len(aplicativo.observadores),1)
    
    def test_adicionarDoisObservador(self):
        aplicativo = Aplicativo()
        observador = ObservadorPalavrasPadrao()
        observador2 = ObservadorPalavrasPadrao()
        aplicativo.adicionar_observador(observador)
        aplicativo.adicionar_observador(observador2)

        self.assertEqual(len(aplicativo.observadores),2)
    
    def test_removerObservador(self):
        aplicativo = Aplicativo()
        observador = ObservadorPalavrasPadrao()
        aplicativo.adicionar_observador(observador)
        aplicativo.remover_observador(observador)

        self.assertEqual(len(aplicativo.observadores),0)

    def test_Notificar(self):
        aplicativo = Aplicativo()
        observador = ObservadorPalavrasPadrao()
        aplicativo.adicionar_observador(observador)
        frase = "Ainda bem que não precisa de Container!"
        aplicativo.notificar_observadores(frase)
        self.assertEqual(observador.total_palavras,7)
        self.assertEqual(len(observador.palavras_pares_caracteres),2)
        self.assertEqual(len(observador.palavras_maiusculas),2)

    def test_NotificarDoisObservadores(self):
        aplicativo = Aplicativo()
        observador = ObservadorPalavrasPadrao()
        observador2 = ObservadorPalavrasPadrao()
        aplicativo.adicionar_observador(observador)
        aplicativo.adicionar_observador(observador2)
        frase = "Ainda bem que não precisa de Container!"
        aplicativo.notificar_observadores(frase)
        self.assertEqual(observador.total_palavras,7)
        self.assertEqual(len(observador.palavras_pares_caracteres),2)
        self.assertEqual(len(observador.palavras_maiusculas),2)
        self.assertEqual(observador2.total_palavras,7)
        self.assertEqual(len(observador2.palavras_pares_caracteres),2)
        self.assertEqual(len(observador2.palavras_maiusculas),2)


if __name__ == "__main__":
    unittest.main()