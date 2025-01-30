from regra_emprestimo_folder.regra_professor import RegraProfessor
from IUsuario import IUsuario

class Professor(IUsuario):
    def __init__(self, id, nome):
        super().__init__(id, nome, RegraProfessor())

    def emprestar_livro(self, livro):
        if self._esta_devendo:
            return "Usuário está em débito."
        data_devolucao = "Indeterminado"
        self._emprestimos.append((livro, data_devolucao))
        return f"Livro {livro} emprestado sem limite de devolução."