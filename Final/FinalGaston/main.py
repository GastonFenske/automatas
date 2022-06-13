import re
ARCHIVO =  'UsuariosWifi.txt'

def show_menu(): 
    return """
[1]Lista todas las sesiones mediante un ID
[2]Listar los inicios de sesión en un usuario en un periodo de tiempo determinado
[3]Tiempo total de la sesión de un usuario, expresada HH:MM:SS
[4]MAC de un usuario, para identificar si se conectó con un dispositivo o varios
[5]Listar las diferentes MAC de un usuario
[6]Listar los usuarios conectados a un AP, mediante la MAC del AP, en una determinada fecha o rango de fecha
[7]Mostrar el tráfico de un usuario (expresado en MB) diferenciando tráfico de
bajada y subida
[8]Listar los AP ordenados por tráfico total
"""

def show_by_user():
    user = input("Ingrese el usuario a buscar: ")
    lines = read_file()
    for line in lines:
        if re.findall(user, line):
            line = show_line(line)
            # print(len(usuario))
            # mac_ap = get_mac_ap(line)
            # date1, date2 = get_date(line)
            # print(date1, date2)
            # info = create_object(line)
            trafic = get_trafic(line)
            # print(trafic)
            # print(info)
            print(line)

def create_object(line):
    id = line[0]
    user = line[1]
    inicio_conexion = line[2]
    fin_conexion = line[3]
    tiempo_sesion = line[4]
    octetos_int = line[5]
    octetos_out = line[6]
    mac_ap = line[7]
    mac_cliente = line[8]
    info_user = Registro(id, user, inicio_conexion, fin_conexion, tiempo_sesion, octetos_int, octetos_out, mac_ap, mac_cliente)
    return info_user

def show_macs_by_user(userId):
    lines = read_file()
    for line in lines:
        if re.findall(userId, line):
            line = show_line(line)
            info = create_object(line)
            print(info.mac_ap)

def read_file():
    archivo = open(ARCHIVO, 'r')
    lines = archivo.readlines()
    archivo.close()
    return lines

def show_line(line):
    line = list(re.split(r';', line))
    return line

def get_mac_ap(line):
    mac_ap = re.search('([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}):UM', line)
    return mac_ap.group(0)

def get_mac(line):
    mac = re.search('([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', line)
    return mac.group(0)

def get_user_id(line):
    user_id = re.search('([\w\d]){16}', line)
    return user_id.group(0)

def get_date(line):
    dates = re.search('((\d{2}\/)+\d{4}) (\d{2}:\d{2})', line)
    return dates.group(0), dates.group(1)

def get_trafic(line):
    down = show_line(line[5])
    up = show_line(line[6])
    print(line)
    return f'Bajada: {down}, Subida: {up}'

class Registro:

    def __init__(self, id, usuario, inicio_conexion, fin_conexion, tiempo_sesion, octetos_int, octeos_out, mac_ap, mac_cliente) -> None:
        self.id = id
        self.usuario = usuario
        self.inicio_conexion = inicio_conexion
        self.fin_conexion = fin_conexion
        self.tiempo_sesion = tiempo_sesion
        self.octetos_int = octetos_int
        self.octeos_out = octeos_out
        self.mac_ap = mac_ap
        self.mac_cliente = mac_cliente

    def __repr__(self):
        return f"ID: {self.id} USUARIO: {self.usuario} INICIO CONEXION: {self.inicio_conexion} FIN CONEXCION:{self.fin_conexion} TIEMPO SESION: {self.tiempo_sesion} OCTETOS INT: {self.octetos_int} OCTETOS OUT: {self.octeos_out} MAC AP: {self.mac_ap} MAC CLIENTE: {self.mac_cliente}"
        

def main():
    l = 'f10be9301bcb139a;csegeview;28/08/2019 10:06;28/08/2019 10:06;12;2354;559;04-18-D6-22-94-E7:UM;48-C7-96-EE-75-1C'
    # print(show_menu())
    show_by_user()
    # show_macs_by_user('csegeview')
    # show_line(abrir_archivo())

if __name__ == '__main__':
    main()

