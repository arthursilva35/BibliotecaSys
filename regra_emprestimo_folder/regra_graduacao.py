from datetime import datetime, timedelta
from regra_emprestimo import RegraEmprestimo

class RegraGraduacao(RegraEmprestimo):
    LIMITE_EMPRESTIMOS = 2
    TEMPO_EMPRESTIMO = 4

    def pode_emprestar(self, usuario):
        return len(usuario.get_emprestimos()) < self.LIMITE_EMPRESTIMOS

    def calcular_prazo(self):
        return datetime.now() + timedelta(days=self.TEMPO_EMPRESTIMO)