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

        def Excluir(self, titulo):
            atual = self.primeiro
            anterior = None
            while atual is not None:
                if atual.titulo == titulo:
                    if anterior is None:
                        self.primeiro = atual.proximo
                    else:
                        anterior.proximo = atual.proximo
                    print("Filme excluído com sucesso!")
                    return
                anterior = atual
                atual = atual.proximo
            print("Filme não encontrado.")

        def Pesquisar (self, titulo, diretor, ano, genero):
            atual = self.primeiro
            while atual is not None:
                if (atual.titulo == titulo and atual.diretor == diretor and 
                    atual.ano == ano and atual.genero == genero):
                    print("Filme encontrado:")
                    atual.mostrar_no()
                    return
                atual = atual.proximo
            print("Filme não encontrado.")
        
        def Relatorio(self):
            pass
        