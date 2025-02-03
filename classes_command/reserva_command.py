from classes_command.command import Command
from sistema_biblioteca import FabricaSistemaBiblioteca
from classes_acoes.reserva import Reserva


class ReservaCommand(Command):
    id_counter = 0

    def executar(self, id_usuario, id_livro):
        sys = FabricaSistemaBiblioteca.get_sistema()
        
        
        usuario = sys.get_usuario_por_id(id_usuario)
        livro = sys.get_livro_por_id(id_usuario)

        if usuario == None:
            return "Não existe usuário com esse Id!"

        if livro == None:
            return "Não existe livro com esse Id!"
        
        ReservaCommand.id_counter += 1
        cur_id = ReservaCommand.id_counter

        novaReserva = Reserva(cur_id, id_usuario, id_livro)


        usuario.adiciona_reserva_na_lista(novaReserva)

        






