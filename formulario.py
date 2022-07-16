import validacao
# View - Tela visual - o que vai para o usuário
def formulari_login():
    usuario_digitado = input("Informe seu usuário: ")
    senha_digitado = input("Informe seu usuário: ")
    validacao.validar_login(usuario_digitado, senha_digitado)