import datetime
from pkgutil import get_data
from requests import session
from filedata import GetData
from utils import FileDescriptor
from model import Register
import re, json


class FileService:

    get_data: GetData = GetData()
    file_descriptor: FileDescriptor = FileDescriptor()

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

    def get_macs_by_user(self, userId) -> set:
        macs: list = []
        lines = self.file_descriptor.read_file()
        lines = self.get_data.get_lines_by_user(userId, lines)
        for line in lines:
            mac = self.get_data.get_mac(line)
            macs.append(mac)
        return set(macs)

    def get_all_mac_ap(self) -> dict:
        lines = self.file_descriptor.read_file()
        macs_ap = {}
        for line in lines:
            mac_ap = self.get_data.get_mac_ap(line)
            if mac_ap not in macs_ap:
                macs_ap[mac_ap] = 1
            else:
                macs_ap[mac_ap] += 1
        return macs_ap

    def order_macs_ap(self) -> dict:
        macs_ap = {k: v for k, v in sorted(self.get_all_mac_ap().items(), key=lambda item: item[1])}
        return macs_ap

    def sesion_time(self, conection_id):
        lines = self.file_descriptor.read_file()
        line = self.get_data.get_line_by_conection_id(conection_id, lines)
        line = self.file_descriptor.show_line(line)
        seconds = self.get_data.get_seconds(line)
        time = datetime.timedelta(seconds=seconds)
        return f"Tiempo de conexion de la sesion con id {conection_id} -> {time}"

    def get_trafic_by_user(self, userId) -> dict:
        lines = self.file_descriptor.read_file()
        lines = self.get_data.get_lines_by_user(userId, lines)
        trafic_down = 0
        trafic_up = 0
        for line in lines:
            trafic_down += self.get_data.get_trafic_down(self.file_descriptor.show_line(line))
            trafic_up += self.get_data.get_trafic_up(self.file_descriptor.show_line(line))
        return {"trafic down MB" : trafic_down/1000000, "trafic up MB": trafic_up/1000000}

    def get_all_user_sessions(self, userId) -> list:
        lines = self.file_descriptor.read_file()
        user_lines = self.get_data.get_lines_by_user(userId, lines)
        user_sessions = []
        for line in user_lines:
            try: 
                id_conection = self.get_data.get_conection_id(line)
                user_sessions.append(id_conection)
            except:
                pass
        return user_sessions


    def get_conection_id_by_date(self, stData, userId) -> list:
        lines = self.file_descriptor.read_file()
        user_lines = self.get_data.get_lines_by_user(userId, lines)
        list_conection_id = []
        for line in user_lines:
            print(line)
            date = self.get_data.get_date(self.file_descriptor.show_line(line))
            print(date)
            if stData == date:
                try:
                    print(self.get_data.get_start_date(self.file_descriptor.show_line(line)))
                    print("agrega inicio de conexion")
                    list_conection_id.append(date)
                except:
                    pass
        return list_conection_id

    # @staticmethod
    # def print_hola() -> list:

    #     nombre = str(input("Ingrese el nombre: "))
    #     lines = []
    #     userId = "f10be9301bcb139a"
    #     lines.append(nombre)
    #     # lines = FileDescriptor.read_file()
    #     # lines = GetData.get_lines_by_user(userId, lines)
    #     return lines
