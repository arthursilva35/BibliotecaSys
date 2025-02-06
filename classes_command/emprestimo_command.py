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
        
        print(GerenciadorReservas._reservas)
        if (usuario.get_tipo_usuario() == "Professor" and livro.get_qtde_exemplares() > 0) or livro.get_qtde_exemplares() - livro.get_qtde_reservas() > 0:
            # Coleta todas as reservas para o livro específico
            reservas = [
                (usuario_id, reserva[1])  # (id_usuario, data_reserva)
                for usuario_id, lista_reservas in GerenciadorReservas._reservas.items()
                for reserva in lista_reservas
                if reserva[0] == livro.get_id()  # Verifica se o ID do livro corresponde
            ]

            print(reservas)

            # Se houver reservas e não houver exemplares disponíveis
            if reservas and livro.get_qtde_exemplares() - livro.get_qtde_reservas() == 0:
                reserva_mais_recente = max(reservas, key=lambda r: r[1])  # Pega a mais recente pela data
                id_usuario_reserva, data_reserva = reserva_mais_recente
                GerenciadorReservas._reservas[id_usuario_reserva].remove((livro.get_id(), data_reserva))
                print(f"Reserva do usuário {id_usuario_reserva} removida.")
                livro.set_qtde_reservas(livro.get_qtde_reservas() - 1)

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
            

