from IObservador import IObservador

class ProfessorObservador(IObservador):
    def notificar(self, livro):
        self.notificacoes += 1
        print(f"Professor {self.id_usuario} foi notificado: O livro '{livro.titulo}' tem mais de 2 reservas.")
