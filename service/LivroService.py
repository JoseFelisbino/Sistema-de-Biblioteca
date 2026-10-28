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


def editar(self, id_livro, novo_titulo=None, novo_autor=None,
    novo_ano=None, novo_disponivel=None, emprestimos=None):
        
    for livro in self.lista:
        if livro.idLivro == id_livro:

            if novo_disponivel is not None:
                if isinstance(novo_disponivel, str):
                    valor = novo_disponivel.strip().lower()

                    if valor not in ("true", "false"):
                        return False

                    novo_disponivel = valor == "true"

                if emprestimos is not None:
                    emprestimo_ativo = any(
                        e.livro.idLivro == id_livro
                        and e.status == "EM ANDAMENTO"
                        for e in emprestimos
                    )

                    if emprestimo_ativo and novo_disponivel:
                        return False

                livro.disponivel = novo_disponivel

            if novo_titulo is not None:
                livro.titulo = novo_titulo

            if novo_autor is not None:
                livro.autor = novo_autor

            if novo_ano is not None:
                livro.ano = novo_ano

            return livro

    return None

    
    def deletar(self, id_livro):
        for livro in self.lista:
            if livro.idLivro == id_livro:
                self.lista.remove(livro)
                return livro

        return None
