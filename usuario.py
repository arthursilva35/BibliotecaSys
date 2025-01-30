from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, id, nome, regra_emprestimo):
        self._id = id
        self._nome = nome
        self._esta_devendo = False
        self._emprestimos = []
        self._reservas = []
        self._regra_emprestimo = regra_emprestimo

    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_esta_devendo(self):
        return self._esta_devendo

    def get_emprestimos(self):
        return self._emprestimos
    
    def get_reservas(self):
        return self._reservas
    
    def set_id(self, id):
        self._id = id

    def set_nome(self, nome):
        self._nome = nome

    def set_esta_devendo(self):
        pass

    def solicitar_emprestimo(self):
        pass

    def solicitar_reserva(self):
        pass