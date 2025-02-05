from abc import ABC, abstractmethod

class IUsuario(ABC):

    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
        self._esta_devendo = False
        self._emprestimos_ativos = []
        self._historico_emprestimos = []
        self._reservas = []
    
    @abstractmethod
    def get_id(self):
        pass
        
    
    @abstractmethod
    def get_nome(self):
        pass
      
    
    @abstractmethod
    def get_esta_devendo(self):
        pass


    @abstractmethod
    def get_emprestimos_ativos(self):
        pass

    
    @abstractmethod
    def get_historico_emprestimos(self):
        pass

    
    @abstractmethod
    def get_reservas(self):
        pass

    
    @abstractmethod
    def mudar_situacao_devedor(self):
        pass

    @abstractmethod
    def ja_tem_livro(self, livro):
        pass

    @abstractmethod
    def ja_tem_reserva(self, livro):
        pass

    @abstractmethod
    def adicionar_reserva(self, livro):
        pass

    @abstractmethod
    def remover_reserva(self, livro_id):
        pass

    @abstractmethod
    def get_tipo_usuario(self):
        pass

    @abstractmethod
    def pode_emprestar(self, livro):
        pass

    @abstractmethod
    def adicionar_emprestimo(self, emprestimo):
        pass

    @abstractmethod
    def adicionar_emprestimo_historico(self, emprestimo):
        pass