from datetime import datetime, timedelta
from regra_emprestimo import RegraEmprestimo

class RegraProfessor(RegraEmprestimo):
    def pode_emprestar(self, usuario):
        return True  # Professores sempre podem pegar emprestado

    def calcular_prazo(self):
        return None  # Prazo indeterminado para professores