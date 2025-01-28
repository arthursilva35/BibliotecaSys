class Livro:
    def __init__(self, id, titulo, editora, autores, edicao, anoPublicacao):
        self.id = id
        self.titulo = titulo
        self.editora = editora
        self.autores = autores
        self.edicao = edicao
        self.anoPublicacao = anoPublicacao
        self.status = "d"

    def get_id(self):
        return self._id

    def get_titulo(self):
        return self._titulo

    def get_editora(self):
        return self._editora

    def get_autores(self):
        return self._autores

    def get_edicao(self):
        return self._edicao

    def get_anoPublicacao(self):
        return self._anoPublicacao

    def get_status(self):
        return self._status
    
    def set_id(self, id):
        self._id = id

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_editora(self, editora):
        self._editora = editora

    def set_autores(self, autores):
        self._autores = autores

    def set_edicao(self, edicao):
        self._edicao = edicao

    def set_anoPublicacao(self, anoPublicacao):
        self._anoPublicacao = anoPublicacao

    def set_status(self, status):
        self._status = status