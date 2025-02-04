from datetime import datetime, timedelta
from .regra_emprestimo import RegraEmprestimo
from classes_biblioteca.livro import Livro
from gerenciador_de_emprestimos import GerenciadorEmprestimos
from gerenciador_de_reservas import GerenciadorReservas

class RegraGraduacao(RegraEmprestimo):
    LIMITE_EMPRESTIMOS = 2
    TEMPO_EMPRESTIMO = 4

    def pode_emprestar(self, usuario, livro: Livro):
        gerenciador_emprestimo = GerenciadorEmprestimos
        gerenciador_reservas = GerenciadorReservas

        if not(livro.get_esta_disponivel()):
            print("Livro indisponível no momento.")
            return False
        
        if gerenciador_emprestimo.usuario_esta_devendo(usuario):
            print("Usuário com empréstimos em atraso. Empréstimo não realizado.")
            return False
        
        if len(usuario.get_emprestimos_ativos()) >= 2:
            print("Usuário já possui 2 livros emprestados atualmente. Empréstimo não realizado.")
            return False
        
        if usuario.ja_tem_livro(livro):
            print("Usuário já possui exemplar do livro. Empréstimo não realizado.")
            return False
        
        if livro.get_qtde_exemplares() <= livro.get_qtde_reservas() and not(gerenciador_reservas.tem_reserva(usuario, livro)):
            print("O livro já atingiu o limite de reservas e o usuário não reservou. Empréstimo não realizado.")
            return False

        return True

    

    def calcular_prazo(self):
        return datetime.now() + timedelta(days=self.TEMPO_EMPRESTIMO)