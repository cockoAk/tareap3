from backend.validacion_usuario import validacion_usuario
from backend.singup import singup
from backend.validacion import validacion
x = input("Ingrese su usuario: ")
y = input("Ingrese su contraseña: ")

validador = validacion_usuario()
if validador.login(x,y):
    print("iniciando sesion...")
else:
    print("usuario invalido, desea crear uno nuevo?")
    respuesta = input("Ingrese 'si' para crear un nuevo usuario: ")
    if respuesta.lower() == 'si':
        x = input("Ingrese su usuario: ")
        y = input("Ingrese su contraseña: ")
        nuevo_usuario = singup()
        corecto = True


        while corecto:
            val = validacion()
            if val.validar_email(x):
                corecto = False

                if val.validar_contrasena(y)[0]:
                    nuevo_usuario.crear_usuario(x, y)
                    print("Usuario creado exitosamente.")
                    corecto = False
                else:
                    print(val.validar_contrasena(y)[1])
            else:
                x = input("Usuario invalido, ingrese un usuario valido: ")
