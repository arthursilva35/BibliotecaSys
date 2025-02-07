import datetime
from  classes_acoes.IAcaoLivro import IAcaoLivro

class Emprestimo(IAcaoLivro):
    def __init__(self, id, id_usuario_responsavel, id_livro, entrega_prevista):
        self._id = id
        self._id_usuario_responsavel = id_usuario_responsavel
        self._id_livro = id_livro
        self._data = datetime.datetime.now()
        self._status = "ativo"
        self._entrega_prevista = entrega_prevista

    def get_id(self):
        return self._id
        
    
    def get_id_usuario_responsavel(self):
        return self._id_usuario_responsavel
      

    def get_id_livro(self):
        return self._id_livro
    
    
    def get_data(self):
        return self._data

    
    def get_status(self):
        return self._status
    
    def mudar_status(self):
        if self._status == "ativo":
            self._status = "inativo"
        else:
            self._status = "ativo"
        
        return None
    
    def get_entrega_prevista(self):
        return self._entrega_prevista