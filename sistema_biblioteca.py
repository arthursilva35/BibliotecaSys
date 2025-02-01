class SistemaBiblioteca:
    def __init__(self):
        self.listaUsuarios = []
        self.listaLivros = []

    def get_usuario_por_id(id):
        pass
    
    def get_livro_por_id(id):
        pass
    

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