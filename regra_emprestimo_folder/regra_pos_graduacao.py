from datetime import datetime, timedelta
from regra_emprestimo import RegraEmprestimo

class RegraPosGraduacao(RegraEmprestimo):
    LIMITE_EMPRESTIMOS = 3
    TEMPO_EMPRESTIMO = 5

    def pode_emprestar(self, usuario):
        return len(usuario.get_emprestimos()) < self.LIMITE_EMPRESTIMOS

    def calcular_prazo(self):
        return datetime.now() + timedelta(days=self.TEMPO_EMPRESTIMO)