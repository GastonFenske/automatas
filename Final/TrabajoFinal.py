import re

def filtrar_por_sesiones(archivo):
    usuario = input("Ingrese el usuario a buscar:")
    read = archivo.read()
    print(read)
    sesiones = re.findall(usuario, read).count(usuario)
    print(f'La cantidad de sesiones del usuario "{usuario}" son {sesiones}')
    archivo.close()


def inicio_de_sesion(archivo):
    # incios de sesion en un periodo de tiempo (rangos de fecha)
    # agregar usuario
    inicio = input("Ingrese el primer dato:")
    fin = input("Ingrese el segundo dato:")
    read = archivo.read()
    sesiones = str(re.findall(inicio, read).count(inicio))
    print(f'La cantidad de sesiones en la fecha "{inicio}" a "{fin}" son "{sesiones}"')
    archivo.close()


def tiempo_sesion(archivo):
    user = input("Ingrese el usuario a buscar:")
    read = archivo.read()
    
    pass


def mac(archivo):
    # ver de cuantos dispositivos se conecto
    pass


def usuarios_ap(archivo):
    #
    pass

def show_line(archivo):
    read = archivo.readline()
    line = str(re.findall(r';', read))
    print(line)
    archivo.close()