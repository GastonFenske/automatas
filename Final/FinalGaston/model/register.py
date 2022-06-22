
class Register:

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

    @staticmethod
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
        info_user = Register(id, user, inicio_conexion, fin_conexion, tiempo_sesion, octetos_int, octetos_out, mac_ap, mac_cliente)
        return info_user