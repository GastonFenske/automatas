import re

def empieza_con_mayuscula(cadena: str) -> str:

    patron = '^[A-Z].*'

    if re.fullmatch(pattern=patron, string=cadena):
        return f'La cadena: [{cadena}] SI empieza con mayuscula'
    return f'La cadena: [{cadena}] NO empieza con mayuscula'

cadena = str(input('Ingrese una cadena: '))
print(empieza_con_mayuscula(cadena=cadena))


