from datetime import datetime, timedelta
from classes_acoes.emprestimo import Emprestimo

class GerenciadorEmprestimos:
    id_counter = 0

    @staticmethod
    def emprestar_livro(usuario, livro):

        tem_reserva = False

        reservas = usuario.get_reservas()

        for reserva in reservas:

            if reserva.get_id_livro() == livro.get_id():
                print(f"Reserva de {livro.get_titulo()} feita por {usuario.get_nome()} cancelada.")
                reserva.mudar_status()
                tem_reserva = True
                break


        
        if not usuario.pode_emprestar():
            print(f"{usuario.get_nome()} não pode realizar empréstimos.")
            return None
        
        if livro.get_qtde_exemplares() == 0 and not tem_reserva:
            print(f"{livro.get_titulo} não possui mais exemplares disponíveis e o usuário não havia reservado.")
            return None
        
        GerenciadorEmprestimos.id_counter += 1
        cur_id = GerenciadorEmprestimos.id_counter

        data_entrega = datetime.now() + timedelta(days=usuario.get_tempo_emprestimo()) 
        
        emp = Emprestimo(cur_id, usuario.get_id(), livro.get_id(), data_entrega)
        usuario.adicionar_emprestimo_ativo(emp)

        print(f"{usuario.get_nome()} pegou emprestado {livro.get_titulo()} com entrega prevista para {data_entrega}")

        return None
    
    @staticmethod
    def devolver_livro(usuario, livro):
       pass