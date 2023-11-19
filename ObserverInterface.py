from abc import ABC, abstractmethod

class observadorInterface(ABC):
    @abstractmethod
    def notificar(self, frase):
        pass