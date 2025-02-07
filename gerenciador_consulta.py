from sistema_biblioteca import FabricaSistemaBiblioteca

class GerenciadorConsulta():
    
    def consulta_reservas(self, usuario):
        sys = FabricaSistemaBiblioteca.get_sistema()
        
        reservas = usuario.get_reservas()


        if len(reservas) == 0:
            print(f"Não há reservas associadas a {usuario.get_nome()}")
            return None
        
        print(f"Reservas encontradas associadas ao usuario {usuario.get_nome()}:")
        
        for res in reservas:

            cur_id = res.get_id_livro()

            livro = sys.get_livro_por_id(cur_id)

            print(f"reserva do livro {livro.get_titulo()} feita em {res.get_data()}, status: {res.get_status()}")
        
        return None
    
    def consulta_emprestimo(self, usuario):
        sys = FabricaSistemaBiblioteca.get_sistema()

        historico_emprestimos = usuario.get_emprestimos()

        if len(historico_emprestimos) == 0:
            print(f"Não há empréstimos associados a {usuario.get_nome()}")
            return None
        
        print(f"Emprestimos encontradas associadas ao usuario {usuario.get_nome()}:")
        
        for emp in historico_emprestimos:

            cur_id = emp.get_id_livro()

            livro = sys.get_livro_por_id(cur_id)

            print(f"emprestimo do livro {livro.get_titulo()} feita em {emp.get_data()}, status: {emp.get_status()}, entrega prevista: {emp.get_entrega_prevista()}")
        
        return None
        
