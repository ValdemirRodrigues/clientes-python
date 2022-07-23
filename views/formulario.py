
# View - Tela visual - o que vai para o usuário
def formulario_login():
    usuario_digitado = input("Informe seu usuário: ")
    senha_digitado = input("Informe seu usuário: ")
    usuario_completo = [usuario_digitado, senha_digitado]
    return usuario_completo

def exibir_mensagem(texto):
    print("\n\n\n")
    print("====================")
    print(texto)
    print("\n\n\n")
    print("====================")    

def menu():
    print(" 1 - Para cadastrar novo cliente")
    print(" 2 - Para listar todos os cliente")
    print(" 3 - Para sair")
    opcao = input("Digite a opção")
    return opcao

def cadastro_cliente():
    nome = input ("Informe o nome:  ")
    telefone = input ("Informe o telefone:  ")
    cliente =[nome,telefone]
    return cliente