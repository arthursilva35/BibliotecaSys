from classes_usuario.aluno_graduacao import AlunoGraduacao
from classes_usuario.aluno_pos_graduacao import AlunoPosGraduacao
from classes_usuario.professor import Professor
from classes_biblioteca.livro import Livro 

class SistemaBiblioteca:
    def __init__(self):
        # tem muitas maneiras melhores de inicializar esses objetos no sistema kkkkkkkk
        self.listaUsuarios = [
            AlunoGraduacao(123, "João Silva"),
            AlunoPosGraduacao(456, "Luiz Fernando Rodrigues"),
            AlunoGraduacao(789, "Pedro Paulo"),
            Professor(100, "Carlos Lucena")]
        
        
        self.listaLivros = [
            Livro(100, "Engenharia de Software", "Addison Wesley", "Ian Sommervile", 6, 2000),
            Livro(101, "UML - Guia do Usuário", "Campus", "Grady Booch, James Rumbaugh, Ivar Jacobson", 7, 2000),
            Livro(200, "Code Complete", "Microsoft Press", "Steve McConnell", 2, 2014),
            Livro(201, "Agile Software Development, Principles, Patterns and Practices", "Prentice Hall", "Robert Martin", 1, 2002),
            Livro(300, "Refactoring: Improving the Design of Existing Code", "Addison Wesley Professional", "Martin Fowler", 1, 1999),
            Livro(301, "Software Metrics: A Rigorous and Practical Approach", "CRC Press", "Norman Fenton, James Bieman", 3, 2014),
            Livro(400, "Design Patterns: Elements of Reusable Object-Oriented Software", "Addison Wesley Professional", "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", 1, 1994), 
            Livro(401, "UML Distilled: A Brief Guide to the Standard Object Modeling Language", "Addison Wesley Professional", "Martin Fowler", 3, 2003)]

    def get_usuario_por_id(self, id):
        for usuario in self.listaUsuarios:
            if usuario.get_id() == id: return usuario
        
        return None # não encontrou o usuário na lista
    
    def get_livro_por_id(self, id):
        for livro in self.listaLivros:
            if livro.get_id() == id: return livro
        
        return None # não encontrou o livro na lista
    

class FabricaSistemaBiblioteca:
    _instancia = None

    @staticmethod # permite referência a _instancia sem usar self
    def get_sistema():
        if FabricaSistemaBiblioteca._instancia is None: # garante a existência de apenas uma instância da classe (padrão Singleton)
            FabricaSistemaBiblioteca._instancia = SistemaBiblioteca()
        return FabricaSistemaBiblioteca._instancia
    


if __name__ == "__main__":
    
    fabrica = FabricaSistemaBiblioteca()

    sistema = fabrica.get_sistema()