from service.UsuarioService import UsuarioService
from service.LivroService import LivroService
from service.EmprestimoService import EmprestimoService


serviceUsuario = UsuarioService()
serviceLivro = LivroService()
serviceEmprestimo = EmprestimoService()


opcao = 0

while opcao != 9:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Cadastrar Livro")
    print("4 - Listar Livros")
    print("5 - Editar Livro")
    print("6 - Deletar Livro")
    print("7 - Realizar empréstimo")
    print("8 - Listar empréstimos de um usuário")
    print("9 - Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do usuário: ")
        matricula = input("Digite a matrícula do usuário: ")
        serviceUsuario.cadastrar(nome, matricula)
        print("Usuário cadastrado com sucesso!")

    elif opcao == 2:
        print("Listando usuários...")
        usuarios = serviceUsuario.listar()
        for usuario in usuarios:
            print(usuario)

    elif opcao == 3:
        titulo = input("Digite o titulo: ")
        autor = input("Digite o autor: ")
        ano = input("Digite o ano: ")
        disponivel = input("Digite o disponivel (true/false): ")
        serviceLivro.cadastrar(titulo, autor, ano, disponivel)
        print("Livro cadastrado com sucesso!")

    elif opcao == 4:
        print("Listando Livros...")
        livros = serviceLivro.listar()
        for livro in livros:
            print(livro)

    elif opcao == 5:
        id_livro = int(input("Digite o ID do livro que deseja editar: "))
        novo_titulo = input("Digite o novo título (ou pressione Enter para manter o atual): ")
        novo_autor = input("Digite o novo autor (ou pressione Enter para manter o atual): ")
        novo_ano = input("Digite o novo ano (ou pressione Enter para manter o atual): ")
        novo_disponivel = input("Digite a nova disponibilidade (true/false) (ou pressione Enter para manter a atual): ")

        if novo_titulo == "":
            novo_titulo = None
        if novo_autor == "":
            novo_autor = None
        if novo_ano == "":
            novo_ano = None
        if novo_disponivel == "":
            novo_disponivel = None

        livro_editado = serviceLivro.editar(id_livro, novo_titulo, novo_autor, novo_ano, novo_disponivel)

        if livro_editado:
            print("Livro editado com sucesso!")
        else:
            print("Livro não encontrado.")

    elif opcao == 6:
        id_livro = int(input("Digite o ID do livro que deseja deletar: "))
        livro_deletado = serviceLivro.deletar(id_livro)
        if livro_deletado:
            print("Livro deletado com sucesso!")
        else:
            print("Livro não encontrado.")

    elif opcao == 7:
        print("\n===== REALIZAR EMPRÉSTIMO =====")

        print("\nLivros cadastrados:")
        for livro in serviceLivro.listar():
            print(livro)

        id_livro = int(input("\nDigite o ID do livro: "))

        livro = next(
            (l for l in serviceLivro.listar()
             if l.idLivro == id_livro),
            None
        )

        print("\nUsuários cadastrados:")
        for usuario in serviceUsuario.listar():
            print(usuario)

        id_usuario = int(input("\nDigite o ID do usuário: "))

        usuario = next(
            (u for u in serviceUsuario.listar()
             if u.idUsuario == id_usuario),
            None
        )

        emprestimo, mensagem = (
            serviceEmprestimo.realizar_emprestimo(livro, usuario)
        )

        print(mensagem)

        if emprestimo:
            print(emprestimo)

    elif opcao == 8:
        print("\n===== EMPRÉSTIMOS POR USUÁRIO =====")

        id_usuario = int(
            input("Digite o ID do usuário: ")
        )

        emprestimos = (
            serviceEmprestimo.listar_por_usuario(id_usuario)
        )

        if emprestimos:
            for emprestimo in emprestimos:
                print(emprestimo)
        else:
            print("Nenhum empréstimo encontrado para esse usuário.")

    elif opcao == 9:
        print("Saindo...")

    else:
        print("Opção inválida! Tente novamente.")

print("Programa finalizado.")
