from classes_usuario.IUsuario import IUsuario
from classes_usuario.IRegraEmprestimo import IRegraEmprestimo
from regra_emprestimo_folder.regra_graduacao import RegraGraduacao

class AlunoGraduacao(IUsuario, IRegraEmprestimo):
    #TEMPO_EMPRESTIMO = 4 
    #LIMITE_EMPRESTIMOS = 2

    
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
        self._esta_devendo = False
        self._emprestimos = []
        self._reservas = []
    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_esta_devendo(self):
        return self._esta_devendo

    def get_emprestimos(self):
        return self._emprestimos
    
    def get_reservas(self):
        return self._reservas
    
    def mudar_situacao_devedor(self):
        if self._esta_devendo == True:
            self._esta_devendo = False
        else:
            self._esta_devendo = True
        
        return None

    def adiciona_reserva_na_lista(self, reserva):
        self._reservas.append(reserva)

        return None
    
    # TO DO: implementar regra especifica pra cada usuário
    def pode_emprestar(self, livro):
        return RegraGraduacao().pode_emprestar(self, livro)