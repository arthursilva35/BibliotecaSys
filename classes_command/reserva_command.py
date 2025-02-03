from classes_command.command import Command
from sistema_biblioteca import FabricaSistemaBiblioteca
from classes_acoes.reserva import Reserva


class ReservaCommand(Command):
    id_counter = 0

    def executar(self, id_usuario, id_livro):
        sys = FabricaSistemaBiblioteca.get_sistema()
        
        
        id_usuario = int(id_usuario)
        id_livro = int(id_livro)
        
        usuario = sys.get_usuario_por_id(id_usuario)
        livro = sys.get_livro_por_id(id_livro)

        if usuario == None:
            print (f"Não existe usuário com o Id: {id_usuario}.")
            return None

        if livro == None:
            print(f"Não existe livro com o Id: {id_livro}.")
            return None

        exemp = livro.get_quatidade_exemplares() 
        

        if( exemp > 0):
        
            ReservaCommand.id_counter += 1
            
            cur_id = ReservaCommand.id_counter

            novaReserva = Reserva(cur_id, id_usuario, id_livro)

            usuario.adiciona_reserva_na_lista(novaReserva)

            livro.set_quatidade_exemplares(exemp - 1)

            print(f"Usuário {usuario.get_nome()} reservou o livro {livro.get_titulo()}!")
        
        else:
            
            print(f"Não há mais exemplares disponíveis do livro{livro.get_titulo()}.")

        return None



