import re

def comentario_valido(cadena: str) -> str:

    patron = '(^[0-9].*7+.*)|(^7.*)|(^[Aa-zZ]).*(p+|P+).*'

    if re.fullmatch(pattern=patron, string=cadena):
        return f'La cadena: [{cadena}] SI cumple con las condiciones'
    return f'La cadena: [{cadena}] NO cumple con las condiciones'

print("""
Si la cadena empieza con un numero debe aparecer al menos una vez el 7
Si la cadena empieza con una letra (mayuscula o minuscula) debe contener al menos una letra p (mayuscula o minuscula)
""")

cadena = str(input('Ingrese una cadena: '))
print(comentario_valido(cadena=cadena))