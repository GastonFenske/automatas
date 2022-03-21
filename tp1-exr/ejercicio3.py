import re

def comentario_valido(cadena: str) -> str:

    patron = '(^#.*)|^"{3}[^"]*"{3}$'

    if re.fullmatch(pattern=patron, string=cadena):
        return f'La cadena: [{cadena}] SI es un comentario valido en Python'
    return f'La cadena: [{cadena}] NO es un comentario valido en Python'

cadena = str(input('Ingrese una cadena: '))
print(comentario_valido(cadena=cadena))
