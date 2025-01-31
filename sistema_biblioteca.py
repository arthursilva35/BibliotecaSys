class SistemaBiblioteca:
    print("oii")


class FabricaSistemaBiblioteca:
    _instancia = None

    @staticmethod # permite referência a _instancia sem usar self
    def get_sistema():
        if FabricaSistemaBiblioteca._instancia is None: # garante a existência de apenas uma instância da classe SistemaBiblioteca (padrão Singleton)
            FabricaSistemaBiblioteca._instancia = SistemaBiblioteca()
        return FabricaSistemaBiblioteca._instancia
    


if __name__ == "__main__":
    
    fabrica = FabricaSistemaBiblioteca()

    sistema = fabrica.get_sistema()


    sistema2 = fabrica.get_sistema()