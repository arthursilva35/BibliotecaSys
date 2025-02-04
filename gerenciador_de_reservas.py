class GerenciadorReservas:
    """Gerenciador universal de reservas - não instanciável."""
    
    _reservas = {}  # Dicionário {codigo_item: [usuarios]}

    @staticmethod
    def adicionar_reserva(usuario: str, item) -> bool:
        """Adiciona uma reserva para um usuário se possível."""
        codigo = item.get_id()
        
        if codigo not in GerenciadorReservas._reservas:
            GerenciadorReservas._reservas[codigo] = []
        
        if usuario in GerenciadorReservas._reservas[codigo]:
            print(f"Usuário {usuario} já reservou o item {codigo}.")
            return False
        
        GerenciadorReservas._reservas[codigo].append(usuario)
        print(f"Reserva do item {codigo} feita com sucesso para {usuario}.")
        return True

    @staticmethod
    def remover_reserva(usuario: str, item) -> bool:
        """Remove a reserva de um usuário para um item."""
        codigo = item.get_id()
        
        if codigo in GerenciadorReservas._reservas and usuario in GerenciadorReservas._reservas[codigo]:
            GerenciadorReservas._reservas[codigo].remove(usuario)
            print(f"Reserva de {usuario} no item {codigo} removida.")
            return True
        
        print(f"Nenhuma reserva encontrada para {usuario} no item {codigo}.")
        return False

    @staticmethod
    def listar_reservas(item) -> list:
        """Lista todos os usuários que reservaram determinado item."""
        return GerenciadorReservas._reservas.get(item.get_id(), [])

    @staticmethod
    def tem_reserva(usuario: str, item) -> bool:
        """Verifica se um usuário tem reserva para um item."""
        return usuario in GerenciadorReservas._reservas.get(item.get_id(), [])