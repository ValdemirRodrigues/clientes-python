# View - Tela visual
def view():
    usuario_digitado = input("Informe seu usuário: ")
    senha_digitado = input("Informe seu usuário: ")

# Model - O que vem no Banco 
def model():
    usuario_BD ='joao'
    senha_BD = '123'

# Controle - A validação
def controller():
    if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
        print ("pode entrar")
    else:
        print ("usuario ou senha invalido")