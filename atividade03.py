class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def __str__(self):
        return f'"{self.__titulo}" por {self.__autor}'


class Biblioteca:
    def __init__(self):
        self.__livros = []  # Atributo privado

    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        print(f'Livro "{livro.get_titulo()}" adicionado à biblioteca.')

    def remover_livro(self, titulo):
        for livro in self.__livros:
            if livro.get_titulo() == titulo:
                self.__livros.remove(livro)
                print(f'Livro "{titulo}" removido da biblioteca.')
                return
        print(f'Livro "{titulo}" não encontrado na biblioteca.')

    def listar_livros(self):
        if not self.__livros:
            print("A biblioteca está vazia.")
        else:
            print("Livros na biblioteca:")
            for livro in self.__livros:
                print(f"- {livro}")

    def __str__(self):
        if not self.__livros:
            return "A biblioteca está vazia."
        resultado = "Livros na biblioteca:\n"
        for livro in self.__livros:
            resultado += f"- {livro}\n"
        resultado += f"Total de livros: {len(self.__livros)}"
        return resultado

#TESTE
meuLivro = Livro("Harry Potter", "J. K. Rowling")
livro1 = Livro("O Hobbit", "J.R.R. Tolkien")
livro2 = Livro("Morte no Nilo", "Agatha Christie")

# Exibindo livro individual
print("Título:", meuLivro.get_titulo())
print("Autor:", meuLivro.get_autor())

# Criando a biblioteca
biblioteca = Biblioteca()

# Adicionando livros
biblioteca.adicionar_livro(meuLivro)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Listando livros
biblioteca.listar_livros()

# Removendo um livro
biblioteca.remover_livro("O Hobbit")

# Usando print(biblioteca)
print("\nExibindo biblioteca com print(biblioteca):")
print(biblioteca)
