from abc import ABC, abstractmethod

class RegraEmprestimo(ABC):
    @abstractmethod
    def pode_emprestar(self, usuario):
        pass

    @abstractmethod
    def calcular_prazo(self):
        pass
