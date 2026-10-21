class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo, data_devolucao):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
    
    def __str__(self):
        return f"Livro: {self.livro}, Usuário: {self.usuario}, Data de Empréstimo: {self.data_emprestimo}, Data de Devolução: {self.data_devolucao}"