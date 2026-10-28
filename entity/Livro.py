
class Livro:
    _contador_id = 1

    def __init__(self, titulo, autor, ano, disponivel):
        self.idLivro = Livro._contador_id
        Livro._contador_id += 1

        self.titulo = titulo
        self.autor = autor
        self.ano = ano

        if isinstance(disponivel, str):
            disponivel = disponivel.strip().lower() == "true"

        self.disponivel = disponivel

    def __str__(self):
        situacao = "Sim" if self.disponivel else "Não"

        return (
            f"ID: {self.idLivro}, "
            f"Título: {self.titulo}, "
            f"Autor: {self.autor}, "
            f"Ano: {self.ano}, "
            f"Disponível: {situacao}"
        )
