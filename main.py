# View - Tela visual - o que vai para o usuário
def view():
    usuario_digitado = input("Informe seu usuário: ")
    senha_digitado = input("Informe seu usuário: ")
    controller(usuario_digitado, senha_digitado)

# Model - O que vem no Banco de Dados(DB)
def model_usuario():
    usuario_BD ='joao'
    return usuario_BD

def model_senha():
    senha_BD = '123'
    return senha_BD

# Controle - A validação
def controller(usuario_digitado, senha_digitado):
    usuario_BD = model_usuario()
    senha_BD = model_senha()
    
    if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
        print ("pode entrar")
    else:
        print ("usuario ou senha invalido")

view()