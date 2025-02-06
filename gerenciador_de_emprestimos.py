from datetime import datetime, timedelta
from gerenciador_de_reservas import GerenciadorReservas

class GerenciadorEmprestimos:

    
    _emprestimos_ativos = {}  # Dicionário {usuario: [(livro, data_devolucao)]}
    _historico_emprestimos = {}  # Dicionário {usuario: [(livro, data_devolucao)]}
    _usuarios_devedores = set()  # Conjunto de usuários em débito

    @staticmethod
    def emprestar_livro(usuario, livro):
        """Tenta emprestar um livro para o usuário"""
        reservas = [
            (usuario_id, reserva[1])  # (id_usuario, data_reserva)
            for usuario_id, lista_reservas in GerenciadorReservas.listar_reservas().items()
            for reserva in lista_reservas
            if reserva[0] == livro.get_id()  # Verifica se o ID do livro corresponde
        ]


        # Se houver reservas e não houver exemplares disponíveis
        if reservas and livro.get_qtde_exemplares() - livro.get_qtde_reservas() == 0:
            reserva_mais_recente = max(reservas, key=lambda r: r[1])  # Pega a mais recente pela data
            id_usuario_reserva, data_reserva = reserva_mais_recente
            # GerenciadorReservas.listar_reservas()[id_usuario_reserva].remove((livro.get_id(), data_reserva))
            GerenciadorReservas._reservas[id_usuario_reserva].remove((livro.get_id(), data_reserva))
            print(f"Reserva do usuário {id_usuario_reserva} removida.")
            livro.set_qtde_reservas(livro.get_qtde_reservas() - 1)


        data_devolucao = datetime.now() + timedelta(days=usuario.get_tempo_emprestimo())
        
        # Registrar empréstimo
        GerenciadorEmprestimos._emprestimos_ativos.setdefault(usuario, []).append((livro, data_devolucao))
        GerenciadorEmprestimos._historico_emprestimos.setdefault(usuario, []).append((livro, data_devolucao))
        livro.set_qtde_exemplares(livro.get_qtde_exemplares() - 1)

        print(f"Livro '{livro.get_titulo()}' emprestado para {usuario.get_nome()} até {data_devolucao.strftime('%d/%m/%Y')}.")

    @staticmethod
    def devolver_livro(usuario, livro):
        """Tenta devolver um livro emprestado"""
        if usuario not in GerenciadorEmprestimos._emprestimos_ativos:
            print(f"Usuário {usuario.get_nome()} não possui empréstimos ativos.")
            return None

        for emprestimo in GerenciadorEmprestimos._emprestimos_ativos[usuario]:
            if emprestimo[0] == livro:
                data_devolucao = emprestimo[1]
                GerenciadorEmprestimos._emprestimos_ativos[usuario].remove(emprestimo)
                
                # Verificar se a devolução está atrasada
                if datetime.now() > data_devolucao:
                    GerenciadorEmprestimos.marcar_usuario_como_devedor(usuario)
                    print(f"Livro '{livro.get_titulo()}' devolvido com atraso. Usuário {usuario.get_nome()} marcado como devedor.")
                    return None
                
                print(f"Livro '{livro.get_titulo()}' devolvido com sucesso.")
                return None

        print(f"Livro '{livro.get_titulo()}' não encontrado nos empréstimos ativos do usuário {usuario.get_nome()}.")
        return None

    @staticmethod
    def listar_emprestimos_ativos(usuario):
        """Lista todos os livros emprestados pelo usuário"""
        return GerenciadorEmprestimos._emprestimos_ativos.get(usuario, [])

    @staticmethod
    def qtde_livros_emprestados(usuario):
        """Retorna a quantidade de livros emprestados pelo usuário"""
        return len(GerenciadorEmprestimos._emprestimos_ativos.get(usuario, []))

    @staticmethod
    def listar_historico_emprestimos(usuario):
        """Lista o histórico de empréstimos do usuário"""
        return GerenciadorEmprestimos._historico_emprestimos.get(usuario, [])

    @staticmethod
    def usuario_possui_livro(usuario, livro):
        """Verifica se o usuário já pegou este livro emprestado"""
        return livro in [emprestimo[0] for emprestimo in GerenciadorEmprestimos._emprestimos_ativos.get(usuario, [])]

    @staticmethod
    def marcar_usuario_como_devedor(usuario):
        """Marca um usuário como devedor"""
        if usuario not in GerenciadorEmprestimos._usuarios_devedores:
            GerenciadorEmprestimos._usuarios_devedores.add(usuario)
            return f"Usuário {usuario} marcado como devedor."
        return f"Usuário {usuario} já está na lista de devedores."

    @staticmethod
    def remover_usuario_devedor(usuario):
        """Remove um usuário da lista de devedores"""
        if usuario in GerenciadorEmprestimos._usuarios_devedores:
            GerenciadorEmprestimos._usuarios_devedores.discard(usuario)
            return f"Usuário {usuario} removido da lista de devedores."
        return f"Usuário {usuario} não está na lista de devedores."

    @staticmethod
    def usuario_esta_devendo(usuario):
        """Verifica se o usuário está em débito"""
        return usuario in GerenciadorEmprestimos._usuarios_devedores