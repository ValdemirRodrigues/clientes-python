# View
usuario_digitado = input("Informe seu usuário: ")
senha_digitado = input("Informe seu usuário: ")

# Model - O que vem no Banco 
usuario_BD ='joao'
senha_BD = '123'

# Controle
if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
    print ("pode entrar")
else:
    print ("usuario ou senha invalido")