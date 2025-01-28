from professor_observador import ProfessorObservador
from livro import Livro
from gerenciador_de_reservas import GerenciadorDeReservas

if __name__ == "__main__":
    # Criando livro
    livro_python = Livro(1, "Python Avançado", "Saraiva", "Joao", "5a", "2021")

    # Criando professores (observadores)
    professor1 = ProfessorObservador("P001")
    professor2 = ProfessorObservador("P002")

    # Criando gerenciador de reservas
    gerenciador = GerenciadorDeReservas()

    # Registrando professores como observadores do livro
    gerenciador.adicionar_observador(livro_python, professor1)
    gerenciador.adicionar_observador(livro_python, professor2)

    # Simulando reservas
    gerenciador.reservar(livro_python)  # 1ª reserva
    gerenciador.reservar(livro_python)  # 2ª reserva
    gerenciador.reservar(livro_python)  # 3ª reserva -> Notificações são enviadas