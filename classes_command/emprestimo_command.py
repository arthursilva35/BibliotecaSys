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
        
        GerenciadorEmprestimos.emprestar_livro(usuario, livro)

