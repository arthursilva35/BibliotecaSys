from IUsuario import IUsuario
from gerenciador_de_emprestimos import GerenciadorEmprestimos
from gerenciador_de_reservas import GerenciadorReservas

class AlunoPosGraduacao(IUsuario):
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
        self._esta_devendo = not self._esta_devendo

    def get_gerenciador_de_emprestimos(self):
        return self._gerenciador_de_emprestimos

    def get_gerenciador_de_reservas(self):
        return self._gerenciador_de_reservas
    
    def add_emprestimo(self, livro, data_devolucao):
        if self._esta_devendo:
            return "Usuário está em débito e não pode pegar empréstimos."
        self._emprestimos.append((livro, data_devolucao))
        return f"Livro '{livro}' emprestado até {data_devolucao.strftime('%d/%m/%Y')}."

    def retornar_emprestimo(self, livro):
        for emprestimo in self._emprestimos:
            if emprestimo[0] == livro:
                self._emprestimos.remove(emprestimo)
                self.add_emprestimo_historico(livro, emprestimo[1])
                return f"Livro '{livro}' devolvido com sucesso."
        return "Livro não encontrado nos empréstimos."

    def add_emprestimo_historico(self, livro, data_devolucao):
        self._historico_emprestimos.append((livro, data_devolucao))

    def add_reserva(self, livro):
        self._reservas.append(livro)
        return f"Livro '{livro}' reservado com sucesso."

    def remover_reserva(self, livro):
        if livro in self._reservas:
            self._reservas.remove(livro)
            return f"Reserva do livro '{livro}' removida com sucesso."
        return "Livro não encontrado nas reservas."