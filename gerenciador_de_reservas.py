from datetime import datetime

class GerenciadorReservas:
    """Gerenciador universal de reservas - não instanciável."""

    _reservas = {}  # Dicionário no formato {id_usuario: [(id_livro, data_reserva)]}

    @staticmethod
    def adicionar_reserva(usuario, livro) -> bool:
        """Adiciona uma reserva para um usuário se possível."""
        print(GerenciadorReservas._reservas)
        id_usuario = usuario.get_id()
        id_livro = livro.get_id()
        
        if id_usuario not in GerenciadorReservas._reservas:
            GerenciadorReservas._reservas[id_usuario] = []
        
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
        print(GerenciadorReservas._reservas.get((usuario.get_id()), []))
        return GerenciadorReservas._reservas.get((usuario.get_id()), [])

    @staticmethod
    def tem_reserva(usuario, livro) -> bool:
        """Verifica se um usuário tem reserva para um livro."""
        return any(reserva[0] == livro.get_id() for reserva in GerenciadorReservas._reservas.get(usuario.get_id(), []))
