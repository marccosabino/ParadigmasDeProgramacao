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

class LivroDigital(Livro): 
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.__formato = formato

    def get_formato(self):
        return self.__formato
    
    def __str__(self):
        return f'"{self.get_titulo()}" por {self.get_autor()} (Formato: {self.__formato})'
    
class LivroFisico(Livro):
    def __init__(self, titulo, autor, num_paginas):
        super().__init__(titulo, autor)
        self.__num_paginas = num_paginas

    def get_num_paginas(self):
        return self.__num_paginas

    def __str__(self):
        return f'"{self.get_titulo()}" por {self.get_autor()} ({self.__num_paginas} páginas)'

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
# Criando diferentes tipos de livros
livro1 = LivroFisico("Dom Casmurro", "Machado de Assis", 220)
livro2 = LivroDigital("1984", "George Orwell", "PDF")
livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")

# Criando a biblioteca
biblioteca = Biblioteca()

# Adicionando livros
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Usando print(biblioteca) para listar tudo
print("\nExibindo biblioteca:")
print(biblioteca)
