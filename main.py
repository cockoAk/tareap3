from backend.validacion_usuario import validacion_usuario
from backend.validacion import validacion
x = input("Ingrese su usuario: ")
y = input("Ingrese su contraseña: ")

validador = validacion_usuario()
if validador.login(x,y):
    print("iniciando sesion...")

    # try login
else:
    print("Usuario o contraseña incorrectos, por favor intente de nuevo.")
    # try again or exitgit checkout -b feature/