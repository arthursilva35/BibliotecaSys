from sistema_biblioteca import  FabricaSistemaBiblioteca

from console import Console


if __name__ == "__main__":


    factory = FabricaSistemaBiblioteca()

    sys = FabricaSistemaBiblioteca.get_sistema()


    console = Console()

    console.iniciar()