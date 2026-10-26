class Livro:

    _contador_id = 1

    def __init__(self, titulo, autor, ano, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel
        self.idLivro = Livro._contador_id

        Livro._contador_id += 1
    
    def __str__(self):
        return f"ID: {self.idLivro}, Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Disponível: {self.disponivel}"
