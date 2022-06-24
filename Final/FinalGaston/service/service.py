import datetime
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
        lines = self.get_data.get_lines_by_user(userId)
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
        lines = self.get_data.get_lines_by_user(userId)
        trafic_down = 0
        trafic_up = 0
        for line in lines:
            trafic_down += self.get_data.get_trafic_down(self.file_descriptor.show_line(line))
            trafic_up += self.get_data.get_trafic_up(self.file_descriptor.show_line(line))
        return {"trafic down MB" : trafic_down/1000000, "trafic up MB": trafic_up/1000000}

    def get_all_user_sessions(self, userId) -> list:
        user_lines = self.get_data.get_lines_by_user(userId)
        user_sessions = []
        for line in user_lines:
            try: 
                id_conection = self.get_data.get_conection_id(line)
                user_sessions.append(id_conection)
            except:
                pass
        return user_sessions

    def get_conection_id_by_date(self, stDate: str, endDate: str, userId: str) -> list:
        user_lines = self.get_data.get_lines_by_user(userId)
        list_conection_id = []
        allow = False
        for line in user_lines:
            date1, date2 = self.get_data.get_date(line)
            if stDate == date1:
                allow = True
            if allow:
                register = Register.create_object(line=self.file_descriptor.show_line(line))
                list_conection_id.append(register.id)
            if endDate == date1:
                return list_conection_id
        return list_conection_id


    def get_users_in_a_mac_ap_by_date(self, mac_ap: str, stDate: str, endDate: str) -> list:
        mac_ap_lines = self.get_data.get_lines_by_mac_ap(mac_ap)
        users = []
        allow = False
        for line in mac_ap_lines:
            date1, date2 = self.get_data.get_date(line)
            if stDate == date1:
                allow = True
            if allow:
                register = Register.create_object(line=self.file_descriptor.show_line(line))
                users.append(register.user)
            if endDate == date1:
                return users
        return users
