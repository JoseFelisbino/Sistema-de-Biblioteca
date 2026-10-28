from datetime import date, timedelta
from entity.Emprestimo import Emprestimo


class EmprestimoService:
    def __init__(self):
        self.lista = []

    def realizar_emprestimo(self, livro, usuario):
        if livro is None:
            return None, "Livro não encontrado."

        if usuario is None:
            return None, "Usuário não encontrado."

        disponivel = livro.disponivel
        if isinstance(disponivel, str):
            disponivel = disponivel.strip().lower() == "true"

        if not disponivel:
            return None, "Este livro não está disponível para empréstimo."

        data_emprestimo = date.today()
        data_devolucao = data_emprestimo + timedelta(days=14)

        emprestimo = Emprestimo(
            livro,
            usuario,
            data_emprestimo,
            data_devolucao
        )

        self.lista.append(emprestimo)

        livro.disponivel = False

        return emprestimo, "Empréstimo realizado com sucesso!"

    def listar_por_usuario(self, id_usuario):
        return [
            emprestimo
            for emprestimo in self.lista
            if emprestimo.usuario.idUsuario == id_usuario
        ]
