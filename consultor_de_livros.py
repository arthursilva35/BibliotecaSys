class ConsultorDeLivros:
    def __init__(self, lista_de_livros):
        self.lista_de_livros = lista_de_livros

    def consultar_livro(self, codigo_livro):
        for livro in self.lista_de_livros.lista:
            if livro.id == codigo_livro:
                self._exibir_informacoes_livro(livro)
                return
        print(f"Livro com código {codigo_livro} não encontrado.")

    def _exibir_informacoes_livro(self, livro):
        print(f"\n Informações do Livro (Código: {livro.id})")
        print(f" - Título: {livro.titulo}")
        print(f" - Editora: {livro.editora}")
        print(f" - Autores: {', '.join(livro.autores)}")
        print(f" - Edição: {livro.edicao}")
        print(f" - Ano de Publicação: {livro.anoPublicacao}")

        # Exibe as reservas do livro
        print(f"\n  Quantidade de Reservas: {len(livro.reservas)}")
        if livro.reservas:
            print("  Usuários que reservaram:")
            for reserva in livro.reservas:
                print(f" - {reserva.usuario.nome}")

        # Exibe informações sobre exemplares
        print("\n  Exemplares:")
        for exemplar in livro.exemplares:
            print(f" - Código: {exemplar.codigo_exemplar}, Status: {exemplar.status}")
            if exemplar.status == "emprestado":
                print(f"   Emprestado para: {exemplar.emprestado_para.nome}")
                print(f"   Data de Empréstimo: {exemplar.data_emprestimo}")
                print(f"   Data de Devolução: {exemplar.data_devolucao}")
