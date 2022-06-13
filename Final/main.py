import TrabajoFinal

ARCHIVO = 'UsuariosWifi.txt'

def main():
    print("""
    [1] Listar todas las sesiones de un usuario
    [2] Listar los inicios de sesion en un periodo de tiempo
    [3] Tiempo total de la sesion de un usuario
    [4] MAC de un usuario, para ver de cuantos dispositivos se conecto
    [5] Listar los uusarios conectados a un AP, mediante MAC del AP
    """)
    opcion = int(input("Ingrese una opcion:"))
    if opcion == 1:
        archivo = open(ARCHIVO, 'r')
        TrabajoFinal.filtrar_por_sesiones(archivo)
    elif opcion == 2:
        archivo = open(ARCHIVO, 'r')
        TrabajoFinal.inicio_de_sesion(archivo)
    elif opcion == 3:
        
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        print("Ingrese una opcion valida")


if __name__ == '__main__':
    main()
