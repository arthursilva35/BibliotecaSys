from classes_command.command import Command
from sistema_biblioteca import FabricaSistemaBiblioteca
from classes_acoes.reserva import Reserva
from gerenciador_de_reservas import GerenciadorReservas


class ReservaCommand(Command):
    id_counter = 1

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
        
        # Adiciona a reserva
        nova_reserva = Reserva(ReservaCommand.id_counter, id_usuario, id_livro)
        
        if not(GerenciadorReservas.adicionar_reserva(usuario, livro)):
            return None
        
        # Reduz a quantidade de exemplares disponíveis
        livro.set_qtde_reservas(livro.get_qtde_reservas() + 1)
        usuario.adicionar_reserva(nova_reserva)
        ReservaCommand.id_counter += 1

        print(f"Reserva confirmada! Usuário {usuario.get_nome()} reservou o livro '{livro.get_titulo()}'.")
        return None