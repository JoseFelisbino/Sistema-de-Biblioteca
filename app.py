from service.UsuarioService import UsuarioService
from service.LivroService import LivroService

serviceUsuario = UsuarioService()


opcao = 0

while opcao != 3:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

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
        print("Encerrando o programa...")

    else:
        print("Opção inválida! Tente novamente.")

print("Programa finalizado.")
