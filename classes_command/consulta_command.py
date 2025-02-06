from classes_command.command import Command
from sistema_biblioteca import FabricaSistemaBiblioteca
from gerenciador_consulta import GerenciadorConsulta

class ConsultaCommand(Command):

    def executar(self, id_usuario):
        sys = FabricaSistemaBiblioteca.get_sistema()

        usuario = sys.get_usuario_por_id(id_usuario)

        if usuario == None:
            print (f"Não existe usuário com o Id: {id_usuario}.")
            return None
        
        GerenciadorConsulta().consulta_reservas(usuario)
        GerenciadorConsulta().consulta_emprestimo(usuario)

