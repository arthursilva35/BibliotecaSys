from classes_command.command import Command
from sistema_biblioteca import FabricaSistemaBiblioteca
from classes_acoes.emprestimo import Emprestimo

class EmprestimoCommand(Command):
    id_counter = 0

    def executar(self, id_usuario, id_livro):
        sys = FabricaSistemaBiblioteca.get_sistema()

        usuario = sys.get_usuario_por_id(id_usuario)
        livro = sys.get_livro_por_id(id_livro)  

        if usuario == None:
            print (f"Não existe usuário com o Id: {id_usuario}.")
            return None

        if livro == None:
            print(f"Não existe livro com o Id: {id_livro}.")
            return None

        strategy_emprestimo = usuario.get_emprestimo_strategy()

        if not strategy_emprestimo.pode_emprestar(usuario, livro):
            print("Empréstimo não permitido.")
            return
        
        if livro.get_qtde_exemplares() > 0:
            EmprestimoCommand.id_counter += 1
            cur_id = EmprestimoCommand.id_counter
            novo_emprestimo = Emprestimo(cur_id, id_usuario, id_livro)
            usuario.adicionar_emprestimo(novo_emprestimo)
            livro.set_qtde_exemplares(livro.get_qtde_exemplares() - 1)
            print(f"Usuário {usuario.get_nome()} pegou emprestado o livro {livro.get_titulo()}!")
        else:
            print(f"Não há mais exemplares disponíveis do livro {livro.get_titulo()}.")
        
        if usuario in [reserva.get_usuario() for reserva in livro.get_reservas()]:
            usuario.remover_reserva(livro.get_id())
            livro.remover_reserva(livro.get_id())