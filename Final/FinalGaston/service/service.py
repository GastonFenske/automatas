import datetime
from requests import session
from filedata import GetData
from utils import FileDescriptor
from model import Register
import re


class FileService:

    # @staticmethod
    # def show_time_by_user():
    #     user = input("Ingrese el usuario a buscar: ")
    #     lines = read_file()
    #     time = 0
    #     for line in lines:
    #         if re.findall(user, line):
    #             line = show_line(line)
    #             time += get_seconds(line)
    #     print(format_time(time))

    # @staticmethod
    # def show_macs_by_user(userId):
    #     lines = FileDescriptor.read_file()
    #     for line in lines:
    #         if re.findall(userId, line):
    #             line = FileDescriptor.show_line(line)
    #             register = Register.create_object(line)
    #             print((register.mac_cliente[1:1]))

    @staticmethod
    def get_macs_by_user(userId) -> set:
        macs: list = []
        lines = FileDescriptor.read_file()
        lines = GetData.get_lines_by_user(userId, lines)
        for line in lines:
            mac = GetData.get_mac(line)
            macs.append(mac)
        return set(macs)


    @staticmethod
    def get_all_mac_ap() -> dict:
        lines = FileDescriptor.read_file()
        macs_ap = {}
        for line in lines:
            mac_ap = GetData.get_mac_ap(line)
            if mac_ap not in macs_ap:
                macs_ap[mac_ap] = 1
            else:
                macs_ap[mac_ap] += 1
        return macs_ap

    @staticmethod
    def order_macs_ap() -> dict:
        macs_ap = {k: v for k, v in sorted(FileService.get_all_mac_ap().items(), key=lambda item: item[1])}
        return macs_ap

    @staticmethod
    def sesion_time(conection_id):
        lines = FileDescriptor.read_file()
        line = GetData.get_line_by_conection_id(conection_id, lines)
        line = FileDescriptor.show_line(line)
        seconds = GetData.get_seconds(line)
        time = datetime.timedelta(seconds=seconds)
        return f"Tiempo de conexion de la sesion con id {conection_id} -> {time}"

    @staticmethod
    def get_trafic_by_user(userId) -> dict:
        lines = FileDescriptor.read_file()
        lines = GetData.get_lines_by_user(userId, lines)
        trafic_down = 0
        trafic_up = 0
        for line in lines:
            trafic_down += GetData.get_trafic_down(FileDescriptor.show_line(line))
            trafic_up += GetData.get_trafic_up(FileDescriptor.show_line(line))
        return {"trafict down MB" : trafic_down/1000000, "trafict up MB": trafic_up/1000000}

    @staticmethod
    def get_all_user_sessions(userId) -> list:
        lines = FileDescriptor.read_file()
        user_lines = GetData.get_lines_by_user(userId, lines)
        user_sessions = []
        for line in user_lines:
            try: 
                id_conection = GetData.get_conection_id(line)
                user_sessions.append(id_conection)
            except:
                pass
        return user_sessions


    # @staticmethod
    # def print_hola() -> list:

    #     nombre = str(input("Ingrese el nombre: "))
    #     lines = []
    #     userId = "f10be9301bcb139a"
    #     lines.append(nombre)
    #     # lines = FileDescriptor.read_file()
    #     # lines = GetData.get_lines_by_user(userId, lines)
    #     return lines
