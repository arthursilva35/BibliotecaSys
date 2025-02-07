from classes_usuario.IUsuario import IUsuario
from classes_usuario.IRegraEmprestimo import IRegraEmprestimo

class AlunoGraduacao(IUsuario, IRegraEmprestimo):
    def __init__(self, id, nome):
        super().__init__(id, nome)
        
        self._LIMITE_EMPRESTIMOS = 2
        self._TEMPO_EMPRESTIMO = 4
    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_esta_devendo(self):
        return self._esta_devendo

    def get_emprestimos(self):
        return self._emprestimos

    def get_emprestimos_ativos(self):
        return self._emprestimos_ativos
    
    def get_reservas(self):
        return self._reservas
    
    def get_tempo_emprestimo(self):
        return self._TEMPO_EMPRESTIMO
    
    def mudar_situacao_devedor(self):
        self._esta_devendo = not self._esta_devendo
        return None

    def adicionar_reserva(self, reserva):
        self._reservas.append(reserva)
        return None
    
    def adicionar_emprestimo_ativo(self, emprestimo):
        self._emprestimos_ativos.append(emprestimo)
        self._emprestimos.append(emprestimo)
        return None
    
    def pode_emprestar(self):
        if (len(self._emprestimos_ativos)) >= self._LIMITE_EMPRESTIMOS: return False
        
        if self._esta_devendo : return False
        
        return True
    
    def get_tempo_emprestimo(self):
        return self._TEMPO_EMPRESTIMO
    
