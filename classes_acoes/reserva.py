import datetime
from  classes_acoes.IAcaoLivro import IAcaoLivro

class Reserva(IAcaoLivro):
    def __init__(self, id, id_usuario_responsavel, id_livro):
        self._id = id
        self._id_usuario_responsavel = id_usuario_responsavel
        self._id_livro = id_livro
        self._data = datetime.datetime.now()
        self._status = "ativa"
    
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
        if self._status == "ativa":
            self._status = "inativa"
        else:
            self._status = "ativa"
        
        return None