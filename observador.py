from abc import ABC, abstractmethod

class Observador(ABC):
    def __init__(self, codigo_usuario):
        self.codigo_usuario = codigo_usuario
        self.notificacoes = 0  # Contador de notificações

    @abstractmethod
    def notificar(self, livro):
        pass