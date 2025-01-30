from abc import ABC, abstractmethod

class Observador(ABC):
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        self.notificacoes = 0  

    @abstractmethod
    def notificar(self, livro):
        pass