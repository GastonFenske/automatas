import re

def cadena_con_numero(cadena: str) -> str:

    patron = '.*([0-9]+).*'

    if re.fullmatch(pattern=patron, string=cadena):
        return f'La cadena: [{cadena}] SI contiene al menos un numero'
    return f'La cadena: [{cadena}] NO contiene al menos un numero'

cadena = str(input('Ingrese una cadena: '))
cadena_con_numero(cadena=cadena)