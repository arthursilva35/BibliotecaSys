from abc import ABC, abstractmethod

class IUsuario(ABC):
    
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
    def get_emprestimos(self):
        pass

    
    @abstractmethod
    def get_reservas(self):
        pass

    
    @abstractmethod
    def mudar_situacao_devedor(self):
        pass

    @abstractmethod
    def adiciona_reserva_na_lista(self):
        pass