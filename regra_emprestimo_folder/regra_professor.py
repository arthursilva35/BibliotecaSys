from datetime import datetime, timedelta
from .regra_emprestimo import RegraEmprestimo
from classes_biblioteca.livro import Livro
from gerenciador_de_emprestimos import GerenciadorEmprestimos
from gerenciador_de_reservas import GerenciadorReservas

class RegraProfessor(RegraEmprestimo):
    TEMPO_EMPRESTIMO = 8
    LIMITE_EMPRESTIMOS = float("inf")

    def pode_emprestar(self, usuario, livro: Livro):
        gerenciador_emprestimo = GerenciadorEmprestimos
        gerenciador_reservas = GerenciadorReservas

        if not(livro.get_esta_disponivel()):
            print("Livro indisponível no momento.")
            return False
        
        if gerenciador_emprestimo.usuario_esta_devendo(usuario):
            print("Usuário com empréstimos em atraso. Empréstimo não realizado.")
            return False
        
        # if usuario.ja_tem_livro(livro):
        if gerenciador_emprestimo.usuario_possui_livro(usuario, livro):
            print("Usuário já possui exemplar do livro. Empréstimo não realizado.")
            return False
        
        return True

    def calcular_prazo(self):
        return datetime.now() + timedelta(days=self.TEMPO_EMPRESTIMO)
    
    def get_tempo_emprestimo(self):
        return self.TEMPO_EMPRESTIMO
    
    def get_limite_emprestimos(self):
        return self.LIMITE_EMPRESTIMOS