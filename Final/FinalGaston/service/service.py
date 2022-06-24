import datetime
from filedata import GetData
from utils import FileDescriptor, Utils
from model import Register
import re, json

class FileService:

    get_data: GetData = GetData()
    file_descriptor: FileDescriptor = FileDescriptor()

    def get_macs_by_user(self, userId=None) -> set:
        userId = str(input("Ingrese el usuario: "))
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

    def sesion_time(self, conection_id=None):
        conection_id = str(input("Ingrese el conection_id: "))
        lines = self.file_descriptor.read_file()
        line = self.get_data.get_line_by_conection_id(conection_id, lines)
        line = self.file_descriptor.show_line(line)
        seconds = self.get_data.get_seconds(line)
        time = datetime.timedelta(seconds=seconds)
        return f"Tiempo de conexion de la sesion con id {conection_id} -> {time}"

    def get_trafic_by_user(self, userId=None) -> dict:
        userId = input("Ingrese el usuario: ")
        lines = self.get_data.get_lines_by_user(userId)
        trafic_down = 0
        trafic_up = 0
        for line in lines:
            trafic_down += self.get_data.get_trafic_down(self.file_descriptor.show_line(line))
            trafic_up += self.get_data.get_trafic_up(self.file_descriptor.show_line(line))
        return {"trafic down MB" : trafic_down/1000000, "trafic up MB": trafic_up/1000000}

    def get_all_user_sessions(self, userId=None) -> list:
        userId = str(input("Ingrese usuario: "))
        user_lines = self.get_data.get_lines_by_user(userId)
        user_sessions = []
        for line in user_lines:
            try: 
                id_conection = self.get_data.get_conection_id(line)
                user_sessions.append(id_conection)
            except:
                pass
        return user_sessions

    def get_by_date_range(self, type_get: str, option_in: str, option_out: str) -> list:
        strategies = {
            "mac": self.get_data.get_lines_by_mac_ap,
            "user": self.get_data.get_lines_by_user
        }
        data = Utils.input_function("fecha inicio", "fecha fin")
        print(data)
        lines = strategies[type_get](option_in)
        results = []
        allow = False
        for line in lines:
            date = self.get_data.get_date(line)
            if data["fecha inicio"] == date[0]:
                allow = True
            if allow:
                register = Register.create_object(line=self.file_descriptor.show_line(line))
                options_out = {
                    "user": register.user,
                    "id": register.id
                }
                results.append(options_out[option_out])
            if data["fecha fin"] == date[0]:
                return results
        return results

    def fun1(self):
        return self.get_by_date_range("user", "csegeview", "id")

    def fun2(self):
        return self.get_by_date_range("mac", "04-18-D6-22-94-E7:UM", "user")


