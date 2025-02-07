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
        
        GerenciadorReservas.adicionar_reserva(usuario, livro)
        
        return None