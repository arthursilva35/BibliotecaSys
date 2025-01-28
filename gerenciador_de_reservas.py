class GerenciadorDeReservas:
    def __init__(self):
        self.reservas = {}  # Dicionário para armazenar {livro: número de reservas}
        self.observadores = {}  # Dicionário {livro: lista de observadores}

    def adicionar_observador(self, livro, observador):
        if livro not in self.observadores:
            self.observadores[livro] = []
        self.observadores[livro].append(observador)

    def remover_observador(self, livro, observador):
        if livro in self.observadores:
            self.observadores[livro].remove(observador)

    def reservar(self, livro):
        if livro not in self.reservas:
            self.reservas[livro] = 0
        self.reservas[livro] += 1

        if self.reservas[livro] > 2:  # Notifica observadores se ultrapassar 2 reservas
            self.notificar_observadores(livro)

    def notificar_observadores(self, livro):
        if livro in self.observadores:
            for observador in self.observadores[livro]:
                observador.notificar(livro)