from abc import ABC, abstractmethod

class IRegraEmprestimo(ABC):

    @abstractmethod
    def pode_emprestar(self, livro):
        pass

    def get_tempo_emprestimo(self):
        pass