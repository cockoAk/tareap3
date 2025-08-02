class validacion:

    def __init__(self):
        pass

def validacion_email(email):
    import re
    # Expresión regular para validar el formato del email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def validacion_contraseña(contraseña):
    # Validar que la contraseña tenga al menos 8 caracteres, una mayúscula, una minúscula y un número
    import re
    if len(contraseña) < 8:
        return False
    if not re.search(r'[A-Z]', contraseña):
        return False
    if not re.search(r'[a-z]', contraseña):
        return False
    if not re.search(r'\d', contraseña):
        return False
    return True