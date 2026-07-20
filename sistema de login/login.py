def cadastro():
    print("Seu nome:")
    usuario = input("-")
    print("sua senha:")
    senha = input("-")
    
usuario, senha = cadastro()

def login(usuario, senha):
    while usuario != tusuario or senha != tsenha:
        print("seu nome:")
        tusuario = input("-")
        print("sua senha:")
        tsenha = input("-") 
        return tusuario, tsenha
    else:
        print("Login realizado com sucesso!")

usuario, senha = cadastro()
login()

