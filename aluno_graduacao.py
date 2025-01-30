from datetime import datetime, timedelta
from regra_emprestimo_folder.regra_graduacao import RegraGraduacao
from usuario import Usuario

class AlunoGraduacao(Usuario):
    TEMPO_EMPRESTIMO = 4 
    LIMITE_EMPRESTIMOS = 2

    def __init__(self, id, nome):
        super().__init__(id, nome, RegraGraduacao())

    def emprestar_livro(self, livro):
        if len(self._emprestimos) >= self.LIMITE_EMPRESTIMOS:
            return "Limite de empréstimos atingido."
        if self._esta_devendo:
            return "Usuário está em débito."
        data_devolucao = datetime.now() + timedelta(days=self.TEMPO_EMPRESTIMO)
        self._emprestimos.append((livro, data_devolucao))
        return f"Livro {livro} emprestado até {data_devolucao.strftime('%d/%m/%Y')}"