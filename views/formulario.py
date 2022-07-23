import controllers.controllerAplicacao as controllerAplicacao
# View - Tela visual - o que vai para o usuário
def formulario_login():
    usuario_digitado = input("Informe seu usuário: ")
    senha_digitado = input("Informe seu usuário: ")
    controllerAplicacao.validar_login(usuario_digitado, senha_digitado)