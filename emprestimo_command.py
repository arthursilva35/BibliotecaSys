from command import Command


class EmprestimoCommand(Command):
    def executar(self, id_usuario, id_livro):
        print(" entrou emprestimo")