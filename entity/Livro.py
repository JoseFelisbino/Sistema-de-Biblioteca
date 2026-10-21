class Livro:
    def __init__(self, titulo, autor, ano, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel
    
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Disponível: {self.disponivel}"