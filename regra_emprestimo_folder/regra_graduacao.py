from datetime import datetime, timedelta
from regra_emprestimo import RegraEmprestimo

class RegraGraduacao(RegraEmprestimo):
    LIMITE_EMPRESTIMOS = 2
    TEMPO_EMPRESTIMO = 4

    def pode_emprestar(self, usuario, livro):
        # gerenciador_emprestimo = usuario.get_gerenciador_de_emprestimos()
        # gerenciador_reservas = usuario.get_gerenciador_de_reservas()

        if not(livro.get_esta_disponivel()):
            print("Livro indisponível no momento.")
            return False
        
        if usuario.get_esta_devendo():
            print("Usuário com empréstimos em atraso. Empréstimo não realizado.")
            return False
        
        if usuario.qtde_livros_emprestados() >= 2:
            print("Usuário já possui 2 livros emprestados atualmente. Empréstimo não realizado.")
            return False
        
        if usuario.usuario_possui_livro():
            print("Usuário já possui exemplar do livro. Empréstimo não realizado.")
            return False
        
        if livro.get_qtde_exemplares() <= livro.get_qtde_reservas() and livro not in usuario.get_reservas():
            print("O livro já atingiu o limite de reservas e o usuário não reservou. Empréstimo não realizado.")
            return False

        return True

    

    def calcular_prazo(self):
        return datetime.now() + timedelta(days=self.TEMPO_EMPRESTIMO)