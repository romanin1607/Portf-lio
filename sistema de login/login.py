def cadastro():
    print("Seu nome:")
    usuario = input("- ")

    print("Sua senha:")
    senha = input("- ")

    return usuario, senha


def login(usuario, senha):
    while True:
        print("Seu nome:")
        tusuario = input("- ")

        print("Sua senha:")
        tsenha = input("- ")

        if usuario == tusuario and senha == tsenha:
            print("Login realizado com sucesso!")
            break
        else:
            print("Usuário ou senha incorretos.")


usuario, senha = cadastro()
login(usuario, senha)
