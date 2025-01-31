from abc import ABC, abstractmethod

class IAcaoLivro(ABC):
    
    @abstractmethod
    def get_id(self):
        pass
        
    
    @abstractmethod
    def get_id_usuario_responsavel(self):
        pass
      
    
    @abstractmethod
    def get_id_livro(self):
        pass
    
    
    @abstractmethod
    def get_data(self):
        pass

    
    @abstractmethod
    def get_status(self):
        pass