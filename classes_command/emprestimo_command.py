from classes_command.command import Command
from sistema_biblioteca import FabricaSistemaBiblioteca
from classes_acoes.emprestimo import Emprestimo
from gerenciador_de_emprestimos import GerenciadorEmprestimos
from gerenciador_de_reservas import GerenciadorReservas
from datetime import datetime, timedelta

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

        if not usuario.pode_emprestar(livro):
            return None
        
        if livro.get_qtde_exemplares() > 0:
            EmprestimoCommand.id_counter += 1
            cur_id = EmprestimoCommand.id_counter
            novo_emprestimo = Emprestimo(cur_id, id_usuario, id_livro)
            
            # Adicionando o empréstimo ao usuário
            usuario.adicionar_emprestimo(novo_emprestimo)
            
            # Atualizando a quantidade de exemplares do livro
            livro.set_qtde_exemplares(livro.get_qtde_exemplares() - 1)
            
            # Adicionando ao GerenciadorEmprestimos
            GerenciadorEmprestimos.emprestar_livro(usuario, livro)
            
            # Adicionando ao histórico de empréstimos do usuário
            usuario.adicionar_emprestimo_historico(novo_emprestimo)
            

        else:
            print(f"Não há mais exemplares disponíveis do livro {livro.get_titulo()}.")
        
        # Verifica se o usuário já tem reserva para o livro específico
        if livro.get_id() in [reserva[0] for reserva in GerenciadorReservas.listar_reservas(usuario)]:
            print(f"Usuário {usuario.get_nome()} tinha uma reserva para o livro {livro.get_titulo()}.")
            
            # Remove a reserva do Gerenciador de Reservas
            GerenciadorReservas.remover_reserva(usuario, livro)
            
            # Remove a reserva do próprio usuário
            usuario.remover_reserva(livro.get_id())
            

