from datetime import datetime

class GerenciadorReservas:
    """Gerenciador universal de reservas - não instanciável."""

    _reservas = {}  # Dicionário no formato {id_usuario: [(id_livro, data_reserva)]}

    @staticmethod
    def adicionar_reserva(usuario, livro) -> bool:
        # Verifica se o livro já foi reservado pelo usuário
        if usuario.ja_tem_reserva(livro):
            print(f"Usuário {usuario.get_nome()} já reservou o livro '{livro.get_titulo()}'.")
            return None
        
        if usuario.ja_tem_livro(livro):
            print(f"Usuário {usuario.get_nome()} já tem o livro '{livro.get_titulo()}' emprestado.")
            return None
        
        # Verifica se há exemplares disponíveis
        if livro.get_qtde_exemplares() == 0:
            print(f"Não há mais exemplares disponíveis do livro '{livro.get_titulo()}'.")
            return None
        
        if livro.get_qtde_reservas() == livro.get_qtde_exemplares():
            print(f"Todos os exemplares do livro '{livro.get_titulo()}' estão reservados.")
            return None
        """Adiciona uma reserva para um usuário se possível."""
        id_usuario = usuario.get_id()
        id_livro = livro.get_id()
        
        if id_usuario not in GerenciadorReservas._reservas:
            GerenciadorReservas._reservas[id_usuario] = []
        
        print(GerenciadorReservas._reservas[id_usuario])
        # Verifica se o usuário já tem 3 reservas
        if len(GerenciadorReservas._reservas[id_usuario]) >= 3:
            print(f"Usuário {usuario.get_nome()} já atingiu o limite de 3 reservas.")
            return False
        
        # Verifica se o livro já está reservado por esse usuário
        if any(reserva[0] == id_livro for reserva in GerenciadorReservas._reservas[id_usuario]):
            print(f"Usuário {usuario.get_nome()} já reservou o livro {livro.get_titulo()}.")
            return False
        
        # Adiciona a reserva com a data atual
        data_reserva = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        GerenciadorReservas._reservas[id_usuario].append((id_livro, data_reserva))

        print(f"Reserva do livro '{livro.get_titulo()}' feita com sucesso para {usuario.get_nome()} em {data_reserva}.")
        return True



    @staticmethod
    def remover_reserva(id_usuario, id_livro):
        if id_usuario in GerenciadorReservas._reservas:
            reservas_usuario = GerenciadorReservas._reservas[id_usuario]
            # Percorre as reservas do usuário e tenta encontrar a que corresponde ao id_livro
            for reserva in reservas_usuario:
                if reserva[0] == id_livro:  # Compara o id_livro
                    reservas_usuario.remove(reserva)  # Remove a reserva
                    print(f"Reserva do livro {id_livro} removida para o usuário {id_usuario}.")
                    print(GerenciadorReservas._reservas[id_usuario])
                    return True  # Sucesso na remoção
        print(f"Reserva não encontrada para o usuário {id_usuario} e o livro {id_livro}.")
        return False  # Caso não encontre a reserva


    @staticmethod
    def listar_reservas_usuario(usuario) -> list:
        """Lista todas as reservas de um usuário."""
        return GerenciadorReservas._reservas.get((usuario.get_id()), [])

    @staticmethod
    def tem_reserva(usuario, livro) -> bool:
        """Verifica se um usuário tem reserva para um livro."""
        return any(reserva[0] == livro.get_id() for reserva in GerenciadorReservas._reservas.get(usuario.get_id(), []))

    @staticmethod
    def listar_reservas() -> dict:
        """Lista todas as reservas de todos os usuários."""
        return GerenciadorReservas._reservas