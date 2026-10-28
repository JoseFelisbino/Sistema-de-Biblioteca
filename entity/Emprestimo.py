
class Emprestimo:
    _contador_id = 1

    def __init__(self, livro, usuario, data_emprestimo, data_devolucao):
        self.idEmprestimo = Emprestimo._contador_id
        Emprestimo._contador_id += 1

        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.data_devolucao_real = None
        self.status = "EM ANDAMENTO"

    def __str__(self):
        devolucao_real = (
            self.data_devolucao_real
            if self.data_devolucao_real
            else "Não devolvido"
        )
        return (
            f"ID: {self.idEmprestimo}, "
            f"Livro: {self.livro.titulo}, "
            f"Usuário: {self.usuario.nome}, "
            f"Empréstimo: {self.data_emprestimo}, "
            f"Devolução prevista: {self.data_devolucao}, "
            f"Devolução efetiva: {devolucao_real}, "
            f"Status: {self.status}"
        )
