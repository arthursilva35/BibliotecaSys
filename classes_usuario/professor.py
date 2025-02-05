from classes_usuario.IUsuario import IUsuario
from regra_emprestimo_folder.regra_professor import RegraProfessor

class Professor(IUsuario):
    def __init__(self, id, nome):
        super().__init__(id, nome)
    
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
    
    def get_tempo_emprestimo(self):
        return RegraProfessor.TEMPO_EMPRESTIMO
    
    def get_limite_emprestimos(self):
        return RegraProfessor.LIMITE_EMPRESTIMOS
    
    def mudar_situacao_devedor(self):
        self._esta_devendo = not self._esta_devendo

    def adicionar_reserva(self, reserva):
        self._reservas.append(reserva)

        return None
    
    def adicionar_emprestimo(self, emprestimo):
        self._emprestimos_ativos.append(emprestimo)

    def adicionar_emprestimo_historico(self, emprestimo):
        self._historico_emprestimos.append(emprestimo)

    def get_emprestimos_ativos(self):
        return self._emprestimos_ativos

    def get_historico_emprestimos(self):
        return self._historico_emprestimos
    
    def remover_reserva(self, id_livro):
        self._reservas = [r for r in self._reservas if r.get_id() != id_livro]
        
        return None
    
    def ja_tem_reserva(self, livro):
        return any([int(e.get_id_livro()) == int(livro.get_id()) for e in self._reservas])
    
    def ja_tem_livro(self, livro):
        return any([int(e.get_id_livro()) == int(livro.get_id()) for e in self._emprestimos_ativos])
    
    def pode_emprestar(self, livro):
        return RegraProfessor().pode_emprestar(self, livro)
    
    def get_tipo_usuario(self):
        return "Professor"