from datetime import datetime
from classes_acoes.reserva import Reserva

class GerenciadorReservas:
    id_counter = 0
    
    @staticmethod
    def adicionar_reserva(usuario, livro):
        GerenciadorReservas.id_counter += 1

        cur_id = GerenciadorReservas.id_counter

        res = Reserva(cur_id, usuario.get_id(), livro.get_id())


        usuario.adicionar_reserva(res)

        print(f"Reserva confirmada! Usuário {usuario.get_nome()} reservou o livro '{livro.get_titulo()}'.")

        return None

    @staticmethod
    def remover_reserva(usuario, livro) -> bool:
        """Remove a reserva de um usuário para um livro."""
        id_usuario = usuario.get_id()
        id_livro = livro.get_id()

        if id_usuario in GerenciadorReservas._reservas:
            for reserva in GerenciadorReservas._reservas[id_usuario]:
                if reserva[0] == id_livro:
                    GerenciadorReservas._reservas[id_usuario].remove(reserva)
                    print(f"Reserva do livro '{livro.get_titulo()}' removida para {usuario.get_nome()}.")
                    return True
        
        print(f"Nenhuma reserva encontrada para {usuario.get_nome()} no livro '{livro.get_titulo()}'.")
        return False

    @staticmethod
    def listar_reservas(usuario) -> list:
        """Lista todas as reservas de um usuário."""
        return GerenciadorReservas._reservas.get((usuario.get_id()), [])

    @staticmethod
    def tem_reserva(usuario, livro) -> bool:
        """Verifica se um usuário tem reserva para um livro."""
        return any(reserva[0] == livro.get_id() for reserva in GerenciadorReservas._reservas.get(usuario.get_id(), []))
