import json
from datetime import date
from pathlib import Path

from entity.Livro import Livro
from entity.Usuario import Usuario
from entity.Emprestimo import Emprestimo


class PersistenciaService:

    def __init__(self, caminho=None):
        pasta_projeto = Path(__file__).resolve().parent.parent

        self.caminho = (
            Path(caminho)
            if caminho
            else pasta_projeto / "data" / "biblioteca.json"
        )

    def salvar(self, service_livro, service_usuario, service_emprestimo):
        self.caminho.parent.mkdir(parents=True, exist_ok=True)

        dados = {
            "livros": [
                {
                    "id": livro.idLivro,
                    "titulo": livro.titulo,
                    "autor": livro.autor,
                    "ano": livro.ano,
                    "disponivel": bool(livro.disponivel),
                }
                for livro in service_livro.listar()
            ],
            "usuarios": [
                {
                    "id": usuario.idUsuario,
                    "nome": usuario.nome,
                    "matricula": usuario.matricula,
                }
                for usuario in service_usuario.listar()
            ],
            "emprestimos": [
                {
                    "id": emprestimo.idEmprestimo,
                    "id_livro": emprestimo.livro.idLivro,
                    "id_usuario": emprestimo.usuario.idUsuario,
                    "data_emprestimo": (
                        emprestimo.data_emprestimo.isoformat()
                    ),
                    "data_devolucao": (
                        emprestimo.data_devolucao.isoformat()
                    ),
                    "data_devolucao_real": (
                        emprestimo.data_devolucao_real.isoformat()
                        if emprestimo.data_devolucao_real
                        else None
                    ),
                    "status": emprestimo.status,
                }
                for emprestimo in service_emprestimo.listar()
            ],
        }

        arquivo_temporario = self.caminho.with_suffix(".tmp")

        arquivo_temporario.write_text(
            json.dumps(
                dados,
                ensure_ascii=False,
                indent=4
            ),
            encoding="utf-8",
        )

        arquivo_temporario.replace(self.caminho)

    def carregar(self, service_livro, service_usuario, service_emprestimo):
        if not self.caminho.exists():
            return False

        try:
            dados = json.loads(
                self.caminho.read_text(encoding="utf-8")
            )

            service_livro.lista.clear()
            service_usuario.lista.clear()
            service_emprestimo.lista.clear()

            livros_por_id = {}

            for item in dados.get("livros", []):
                livro = Livro(
                    item["titulo"],
                    item["autor"],
                    item["ano"],
                    bool(item["disponivel"]),
                )

                livro.idLivro = int(item["id"])
                service_livro.lista.append(livro)
                livros_por_id[livro.idLivro] = livro

            usuarios_por_id = {}

            for item in dados.get("usuarios", []):
                usuario = Usuario(
                    item["nome"],
                    item["matricula"]
                )

                usuario.idUsuario = int(item["id"])
                service_usuario.lista.append(usuario)
                usuarios_por_id[usuario.idUsuario] = usuario

            Livro._contador_id = max(livros_por_id, default=0) + 1
            Usuario._contador_id = max(usuarios_por_id, default=0) + 1

            maior_id_emprestimo = 0

            for item in dados.get("emprestimos", []):
                livro = livros_por_id.get(int(item["id_livro"]))
                usuario = usuarios_por_id.get(int(item["id_usuario"]))

                if livro is None or usuario is None:
                    continue

                emprestimo = Emprestimo(
                    livro,
                    usuario,
                    date.fromisoformat(item["data_emprestimo"]),
                    date.fromisoformat(item["data_devolucao"]),
                )

                emprestimo.idEmprestimo = int(item["id"])

                data_real = item.get("data_devolucao_real")

                emprestimo.data_devolucao_real = (
                    date.fromisoformat(data_real)
                    if data_real
                    else None
                )

                emprestimo.status = item.get(
                    "status",
                    "EM ANDAMENTO"
                )

                service_emprestimo.lista.append(emprestimo)

                maior_id_emprestimo = max(
                    maior_id_emprestimo,
                    emprestimo.idEmprestimo
                )

            Emprestimo._contador_id = maior_id_emprestimo + 1

            livros_emprestados = {
                e.livro.idLivro
                for e in service_emprestimo.lista
                if e.status == "EM ANDAMENTO"
            }

            for livro in service_livro.lista:
                if livro.idLivro in livros_emprestados:
                    livro.disponivel = False

            return True

        except (
            OSError,
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError
        ) as erro:
            raise RuntimeError(
                f"Não foi possível carregar os dados: {erro}"
            ) from erro
