from service.UsuarioService import UsuarioService
from service.LivroService import LivroService

serviceUsuario = UsuarioService()
serviceLivro = LivroService()


opcao = 0

while opcao != 4:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Cadastrar Livro")
    print("4 - Sair")

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
        print("Saindo...")

    else:
        print("Opção inválida! Tente novamente.")

print("Programa finalizado.")
