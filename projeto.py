# Classe que representa um nó (filme) da lista encadeada
class No:
    def __init__(self, titulo, diretor, ano, genero):
        # Atributos do filme
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.genero = genero
        # Ponteiro para o próximo nó da lista
        self.proximo = None
    
    # Método para exibir os dados do filme
    def mostrar_no(self):
        print(f"Título: {self.titulo}")
        print(f"Diretor: {self.diretor}")
        print(f"Ano: {self.ano}")
        print(f"Gênero: {self.genero}")


# Classe que representa o catálogo (lista encadeada de filmes)
class CatalogoFilmes:
    def __init__(self):
        # Inicialmente a lista está vazia
        self.primeiro = None

    def povoar_catalogo(self, quantidade=1000):
        print(f"Povoando o catálogo com {quantidade} filmes...")
        for i in range(1, quantidade + 1):
            for a in range(1000):
                id = id + 1
            titulo = f"Filme Exemplo {i}"
            diretor = f"Diretor {i}"
            ano = str(1900 + (i % 125))  # Gera anos variados entre 1900 e 2025
            genero = "Gênero de Teste"
            
            self.Incluir(titulo, diretor, ano, genero)
        print("\nCarga de dados finalizada!")

    # Método para incluir um novo filme no final da lista
    def Incluir(self, titulo, diretor, ano, genero):
        # Cria um novo nó com os dados informados
        novo_filme = No(titulo, diretor, ano, genero)

        # Se a lista estiver vazia, o novo filme vira o primeiro
        if self.primeiro is None:
            self.primeiro = novo_filme
        else:
            # Percorre até o último nó
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            # Liga o último nó ao novo filme
            atual.proximo = novo_filme

        print("Filme incluído com sucesso!")

    # Método para excluir um filme pelo título e diretor
    def Excluir(self, titulo, diretor):
        atual = self.primeiro
        anterior = None

        # Percorre a lista
        while atual is not None:
            # Verifica se encontrou o filme
            if (atual.titulo == titulo and atual.diretor == diretor):
                # Se for o primeiro nó
                if anterior is None:
                    self.primeiro = atual.proximo
                else:
                    # "Pula" o nó atual, removendo-o da lista
                    anterior.proximo = atual.proximo

                print("Filme excluído com sucesso!")
                return

            # Avança na lista
            anterior = atual
            atual = atual.proximo

        # Caso não encontre o filme
        print("Filme não encontrado.")

    # Método para pesquisar um filme
    def Pesquisar(self, titulo, diretor):
        atual = self.primeiro

        # Percorre a lista
        while atual is not None:
            # Se encontrar o filme
            if (atual.titulo == titulo and atual.diretor == diretor):
                print("Filme encontrado:\n")
                atual.mostrar_no()
                return

            atual = atual.proximo
        import timeit
        #%timeit 
        # Caso não encontre
        print("Filme não encontrado.")

    # Método para exibir todos os filmes do catálogo
    def Relatorio(self):
        # Verifica se a lista está vazia
        if self.primeiro is None:
            print("Nenhum filme cadastrado no catálogo.")
            return

        print("=" * 40)
        print("       CATÁLOGO DE FILMES")
        print("=" * 40)

        atual = self.primeiro
        contador = 1

        # Percorre todos os nós da lista
        while atual is not None:
            print(f"\nFilme #{contador}")
            print("-" * 40)
            atual.mostrar_no()
            atual = atual.proximo
            contador += 1

        print("=" * 40)
        print(f"Total de filmes: {contador - 1}")


# Função principal com menu interativo
def menu():
    # Cria uma instância do catálogo
    catalogo = CatalogoFilmes()

    # Loop infinito até o usuário sair
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

        # Lê a opção do usuário
        opcao = input("Escolha uma opção: ").strip()

        # Opção 1: incluir filme
        if opcao == "1":
            print("\n--- INCLUIR FILME ---")
            titulo = input("Título: ").strip()
            diretor = input("Diretor: ").strip()
            ano = input("Ano: ").strip()
            genero = input("Gênero: ").strip()
            catalogo.Incluir(titulo, diretor, ano, genero)

        # Opção 2: excluir filme
        elif opcao == "2":
            print("\n--- EXCLUIR FILME ---")
            titulo = input("Título do filme a excluir: ").strip()
            diretor = input("Diretor do filme: ").strip()
            catalogo.Excluir(titulo, diretor)

        # Opção 3: pesquisar filme
        elif opcao == "3":
            print("\n--- PESQUISAR FILME ---")
            titulo = input("\nTítulo: ").strip()
            diretor = input("Diretor: ").strip()
            catalogo.Pesquisar(titulo, diretor)

        # Opção 4: mostrar relatório
        elif opcao == "4":
            print()
            catalogo.Relatorio()

        # Opção 0: sair do programa
        elif opcao == "0":
            print("\nSaindo... Até logo!")
            break

        # Caso digite uma opção inválida
        else:
            print("\nOpção inválida. Tente novamente.")


# Executa o programa
menu()