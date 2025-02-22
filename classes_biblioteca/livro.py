import random

class Livro:
    def __init__(self, id, titulo, editora, autores, edicao, anoPublicacao, qtdExemplares):
        self._id = id
        self._titulo = titulo
        self._editora = editora
        self._autores = autores
        self._edicao = edicao
        self._anoPublicacao = anoPublicacao
        self._qtdExemplares = qtdExemplares
        self._status = "d"

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
    
    def get_qtde_exemplares(self):
        return self._qtdExemplares

    def set_qtde_exemplares(self, qtd):
        self._qtdExemplares = qtd
        return None

    def get_status(self):
        return self._status

    def change_status(self):
        if self._status ==  "d":
            self._status = "n"
        else:
            self._status = "d"
        return None