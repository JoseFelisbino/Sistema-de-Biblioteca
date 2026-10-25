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
        