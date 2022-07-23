
# Model - O que vem no Banco de Dados(DB)
def model_usuario():
    arquivo= open("models\\usuarios.txt","r+")
    conteudo = arquivo.readlines()
   
    for linha in conteudo:
        usuario_senha = linha.split(";")
   
    usuario_BD = usuario_senha[0]
    return usuario_BD

def model_senha():
    arquivo= open("models\\usuarios.txt","r+")
    conteudo = arquivo.readlines()
   
    for linha in conteudo:
        usuario_senha = linha.split(";")
    senha_BD = usuario_senha[1]
    return senha_BD

def model_cadastro_cliente(cliente)
    print("cadastrado")