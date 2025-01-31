from IObservador import IObservador

class ProfessorObservador(IObservador):
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        self.notificacoes = 0  
    
    def notificar(self, livro):
        self.notificacoes += 1
        print(f"Professor {self.id_usuario} foi notificado: O livro '{livro.titulo}' tem mais de 2 reservas.")
