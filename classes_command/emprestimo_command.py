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
            print("Empréstimo não permitido.")
            return
        
        if livro.get_qtde_exemplares() > 0:
            EmprestimoCommand.id_counter += 1
            cur_id = EmprestimoCommand.id_counter
            novo_emprestimo = Emprestimo(cur_id, id_usuario, id_livro)
            
            # Adicionando o empréstimo ao usuário
            usuario.adicionar_emprestimo(novo_emprestimo)
            
            # Atualizando a quantidade de exemplares do livro
            livro.set_qtde_exemplares(livro.get_qtde_exemplares() - 1)
            
            # Adicionando ao GerenciadorEmprestimos
            data_devolucao = datetime.now() + timedelta(days=GerenciadorEmprestimos.TEMPO_EMPRESTIMO)
            GerenciadorEmprestimos._emprestimos_ativos.setdefault(usuario.get_nome(), []).append((livro.get_titulo(), data_devolucao))
            GerenciadorEmprestimos._historico_emprestimos.setdefault(usuario.get_nome(), []).append((livro.get_titulo(), data_devolucao))
            
            # Adicionando ao histórico de empréstimos do usuário
            usuario.adicionar_emprestimo_historico(novo_emprestimo)
            
            print(f"Usuário {usuario.get_nome()} pegou emprestado o livro {livro.get_titulo()}!")

        else:
            print(f"Não há mais exemplares disponíveis do livro {livro.get_titulo()}.")
        
        if usuario in [reserva.get_usuario() for reserva in GerenciadorReservas.listar_reservas(livro)]:
            usuario.remover_reserva(livro.get_id())
            livro.remover_reserva(livro.get_id())