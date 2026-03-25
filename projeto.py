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
            pass
        def Pesquisar (self, titulo, diretor, ano, genero):
            pass