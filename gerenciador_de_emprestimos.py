from datetime import datetime, timedelta

class GerenciadorEmprestimos:
    TEMPO_EMPRESTIMO = 4  # Dias de empréstimo
    LIMITE_EMPRESTIMOS = 2
    
    _emprestimos_ativos = {}  # Dicionário {usuario: [(livro, data_devolucao)]}
    _historico_emprestimos = {}  # Dicionário {usuario: [(livro, data_devolucao)]}
    _usuarios_devedores = set()  # Conjunto de usuários em débito

    @staticmethod
    def emprestar_livro(usuario, livro):
        """Tenta emprestar um livro para o usuário"""
        
        if usuario in GerenciadorEmprestimos._usuarios_devedores:
            return "Usuário está em débito."

        if GerenciadorEmprestimos.usuario_possui_livro(usuario, livro):
            return "Usuário já possui este livro emprestado."

        if len(GerenciadorEmprestimos._emprestimos_ativos.get(usuario, [])) >= GerenciadorEmprestimos.LIMITE_EMPRESTIMOS:
            return "Limite de empréstimos atingido."

        data_devolucao = datetime.now() + timedelta(days=GerenciadorEmprestimos.TEMPO_EMPRESTIMO)
        
        # Registrar empréstimo
        GerenciadorEmprestimos._emprestimos_ativos.setdefault(usuario, []).append((livro, data_devolucao))
        GerenciadorEmprestimos._historico_emprestimos.setdefault(usuario, []).append((livro, data_devolucao))

        return f"Livro '{livro}' emprestado para {usuario} até {data_devolucao.strftime('%d/%m/%Y')}."

    @staticmethod
    def devolver_livro(usuario, livro):
        """Tenta devolver um livro emprestado"""
        if usuario not in GerenciadorEmprestimos._emprestimos_ativos:
            return "Usuário não possui empréstimos ativos."

        for emprestimo in GerenciadorEmprestimos._emprestimos_ativos[usuario]:
            if emprestimo[0] == livro:
                GerenciadorEmprestimos._emprestimos_ativos[usuario].remove(emprestimo)
                return f"Livro '{livro}' devolvido com sucesso."

        return "Livro não encontrado nos empréstimos ativos do usuário."

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
        return any(emprestimo[0] == livro for emprestimo in GerenciadorEmprestimos._emprestimos_ativos.get(usuario, []))

    @staticmethod
    def marcar_usuario_como_devedor(usuario):
        """Marca um usuário como devedor"""
        GerenciadorEmprestimos._usuarios_devedores.add(usuario)

    @staticmethod
    def remover_usuario_devedor(usuario):
        """Remove um usuário da lista de devedores"""
        GerenciadorEmprestimos._usuarios_devedores.discard(usuario)

    @staticmethod
    def usuario_esta_devendo(usuario):
        """Verifica se o usuário está em débito"""
        return usuario in GerenciadorEmprestimos._usuarios_devedores
