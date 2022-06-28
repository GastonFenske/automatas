import datetime
from filedata import DataFilter
from utils import FileDescriptor, Utils
from model import Register

class FileService:

    get_data: DataFilter = DataFilter()
    file_descriptor: FileDescriptor = FileDescriptor()

    def get_macs_by_user(self, user_id=None) -> set:
        user_id = str(input("Ingrese el usuario: "))
        macs: list = []
        lines = self.get_data.get_lines_by_user(user_id)
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

    def sesion_time(self):
        user_id = str(input("Ingrese el user: "))
        lines = self.get_data.get_lines_by_user(user_id)
        time = 0
        for line in lines:
            time += self.get_data.get_seconds(self.file_descriptor.show_line(line))
        time = datetime.timedelta(seconds=time)
        return time

    def get_trafic_by_user(self, user_id=None) -> dict:
        user_id = input("Ingrese el usuario: ")
        lines = self.get_data.get_lines_by_user(user_id)
        trafic_down = 0
        trafic_up = 0
        for line in lines:
            trafic_down += self.get_data.get_trafic_down(self.file_descriptor.show_line(line))
            trafic_up += self.get_data.get_trafic_up(self.file_descriptor.show_line(line))
        return {"trafic down MB" : trafic_down/1000000, "trafic up MB": trafic_up/1000000}

    def get_all_user_sessions(self, user_id=None) -> list:
        user_id = str(input("Ingrese usuario: "))
        user_lines = self.get_data.get_lines_by_user(user_id)
        user_sessions = []
        for line in user_lines:
            try: 
                id_conection = self.get_data.get_conection_id(line)
                user_sessions.append(id_conection)
            except:
                pass
        return user_sessions

    def get_by_date_range(self, type_get) -> list:
        data_input = Utils.input_function("fecha inicio", "fecha fin", "parametro")
        lines = type_get(data_input["parametro"])
        results = []
        for line in lines:
            date = self.get_data.get_date(line)
            date = datetime.datetime.strptime(date[0], "%d/%m/%Y %H:%M")
            start_date = datetime.datetime.strptime(data_input["fecha inicio"], "%d/%m/%Y %H:%M")
            end_date = datetime.datetime.strptime(data_input["fecha fin"], "%d/%m/%Y %H:%M")
            if start_date <= date <= end_date:
                register = Register.create_object(line=self.file_descriptor.show_line(line))
                results.append(register)
            if end_date == date:
                break
        return results

    def strategies(self, strategy):
        strategies = {
            "mac": self.get_data.get_lines_by_mac_ap,
            "user": self.get_data.get_lines_by_user
        }
        return  strategies[strategy]

    def get_sessions_by_user_and_date(self) -> list:
        objects = self.get_by_date_range(self.strategies("user"))
        return [o.id for o in objects]

    def get_users_by_macap_and_date(self) -> list:
        objects = self.get_by_date_range(self.strategies("mac"))
        return [o.user for o in objects]


