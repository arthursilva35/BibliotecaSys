from classes_command.command import Command
from sistema_biblioteca import FabricaSistemaBiblioteca
from classes_acoes.reserva import Reserva
from gerenciador_de_reservas import GerenciadorReservas


class ReservaCommand(Command):
    id_counter = 0

    def executar(self, id_usuario, id_livro):
        sys = FabricaSistemaBiblioteca.get_sistema()
        
        id_usuario = int(id_usuario)
        id_livro = int(id_livro)
        
        usuario = sys.get_usuario_por_id(id_usuario)
        livro = sys.get_livro_por_id(id_livro)

        if usuario is None:
            print(f"Não existe usuário com o Id: {id_usuario}.")
            return None

        if livro is None:
            print(f"Não existe livro com o Id: {id_livro}.")
            return None

        # Verifica se o usuário já atingiu o limite de reservas
        if len(usuario.get_reservas()) >= 3:
            print(f"Usuário {usuario.get_nome()} já possui 3 reservas simultâneas. Reserva não permitida.")
            return None
        
        # Verifica se o livro já foi reservado pelo usuário
        if usuario.ja_tem_reserva(livro):
            print(f"Usuário {usuario.get_nome()} já reservou o livro '{livro.get_titulo()}'.")
            return None
        
        # Verifica se há exemplares disponíveis
        if livro.get_qtde_exemplares() == 0:
            print(f"Não há mais exemplares disponíveis do livro '{livro.get_titulo()}'.")
            return None

        # Adiciona a reserva
        ReservaCommand.id_counter += 1
        nova_reserva = Reserva(ReservaCommand.id_counter, id_usuario, id_livro)
        
        usuario.adicionar_reserva(nova_reserva)
        GerenciadorReservas.adicionar_reserva(usuario, livro)

        # Reduz a quantidade de exemplares disponíveis
        livro.set_qtde_exemplares(livro.get_qtde_exemplares() - 1)

        print(f"Reserva confirmada! Usuário {usuario.get_nome()} reservou o livro '{livro.get_titulo()}'.")
        return None