from entity.Livro import Livro

class LivroService:
    def __init__(self):
        self.lista = []
    
    def cadastrar(self, titulo, autor, ano, disponivel):
        novoLivro = Livro(titulo, autor, ano, disponivel)
        self.lista.append(novoLivro)
        return novoLivro
    
    def listar(self):
        return self.lista

    def editar(self, id_livro, novo_titulo=None, novo_autor=None, novo_ano=None, novo_disponivel=None):
        for livro in self.lista:
            if livro.idLivro == id_livro:

                if novo_titulo is not None:
                    livro.titulo = novo_titulo
                if novo_autor is not None:
                    livro.autor = novo_autor
                if novo_ano is not None:
                    livro.ano = novo_ano
                if novo_disponivel is not None:
                    livro.disponivel = novo_disponivel

                return livro

        return None
