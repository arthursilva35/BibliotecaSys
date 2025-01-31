from abc import ABC, abstractmethod

class IObservador(ABC):

    @abstractmethod
    def notificar(self, livro):
        pass