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

        qtd_exemp = livro.get_qtde_exemplares()

        livro.set_qtde_exemplares(qtd_exemp -1)


        print(f"Reserva confirmada! Usuário {usuario.get_nome()} reservou o livro '{livro.get_titulo()}'.")

        return None

    @staticmethod
    def remover_reserva(usuario, livro):
        pass
