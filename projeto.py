class No:
    def __init__(self, titulo, diretor, ano, genero):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.genero = genero
        self.proximo = None
    
    def mostrar_no(self):
        print(f"Título: {self.titulo}")
        print(f"Diretor: {self.diretor}")
        print(f"Ano: {self.ano}")
        print(f"Gênero: {self.genero}")


class CatalogoFilmes:
    def __init__(self):
        self.primeiro = None

    def Incluir(self, titulo, diretor, ano, genero):
        novo_filme = No(titulo, diretor, ano, genero)

        if self.primeiro is None:
            self.primeiro = novo_filme
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_filme
        print("Filme incluído com sucesso!")

    def Excluir(self, titulo, diretor):
        atual = self.primeiro
        anterior = None
        while atual is not None:
            if (atual.titulo == titulo and atual.diretor == diretor):
                if anterior is None:
                    self.primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                print("Filme excluído com sucesso!")
                return
            anterior = atual
            atual = atual.proximo
        print("Filme não encontrado.")

    def Pesquisar(self, titulo, diretor):
        atual = self.primeiro
        while atual is not None:
            if (atual.titulo == titulo and atual.diretor == diretor):
                print("Filme encontrado:\n")
                atual.mostrar_no()
                return
            atual = atual.proximo
        print("Filme não encontrado.")

    def Relatorio(self):
        if self.primeiro is None:
            print("Nenhum filme cadastrado no catálogo.")
            return

        print("=" * 40)
        print("       CATÁLOGO DE FILMES")
        print("=" * 40)

        atual = self.primeiro
        contador = 1

        while atual is not None:
            print(f"\nFilme #{contador}")
            print("-" * 40)
            atual.mostrar_no()
            atual = atual.proximo
            contador += 1

        print("=" * 40)
        print(f"Total de filmes: {contador - 1}")


def menu():
    catalogo = CatalogoFilmes()

    while True:
        print("\n" + "=" * 40)
        print("      CATÁLOGO DE FILMES")
        print("=" * 40)
        print("1 - Incluir filme")
        print("2 - Excluir filme")
        print("3 - Pesquisar filme")
        print("4 - Relatório")
        print("0 - Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- INCLUIR FILME ---")
            titulo = input("Título: ").strip()
            diretor = input("Diretor: ").strip()
            ano = input("Ano: ").strip()
            genero = input("Gênero: ").strip()
            catalogo.Incluir(titulo, diretor, ano, genero)

        elif opcao == "2":
            print("\n--- EXCLUIR FILME ---")
            titulo = input("Título do filme a excluir: ").strip()
            diretor = input("Diretor do filme: ").strip()
            catalogo.Excluir(titulo, diretor)

        elif opcao == "3":
            print("\n--- PESQUISAR FILME ---")
            titulo = input("\nTítulo: ").strip()
            diretor = input("Diretor: ").strip()
            catalogo.Pesquisar(titulo, diretor)

        elif opcao == "4":
            print()
            catalogo.Relatorio()

        elif opcao == "0":
            print("\nSaindo... Até logo!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


menu()
