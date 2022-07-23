import models.banco as banco
import views.formulario as view
# Controle - A validação
def validar_login(usuario_completo):
    usuario_BD = banco.model_usuario()
    senha_BD = banco.model_senha()
    
    if usuario_completo[0]== usuario_BD and usuario_completo[1] == senha_BD:
        print ("pode entrar")
    else:
        print ("usuario ou senha invalido")

def iniciar():
    usuario_completo = view.formulario_login()
    validar_login(usuario_completo)
    #validar_login(viw.formulario_login())