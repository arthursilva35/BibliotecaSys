from datetime import datetime, timedelta
from regra_emprestimo_folder.regra_graduacao import RegraGraduacao
from IUsuario import IUsuario
class AlunoGraduacao(IUsuario):
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


'''    def emprestar_livro(self, livro):
        if len(self._emprestimos) >= self.LIMITE_EMPRESTIMOS:
            return "Limite de empréstimos atingido."
        if self._esta_devendo:
            return "Usuário está em débito."
        data_devolucao = datetime.now() + timedelta(days=self.TEMPO_EMPRESTIMO)
        self._emprestimos.append((livro, data_devolucao))
        return f"Livro {livro} emprestado até {data_devolucao.strftime('%d/%m/%Y')}"'''