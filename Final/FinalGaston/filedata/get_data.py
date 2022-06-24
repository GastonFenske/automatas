import re
from utils import FileDescriptor

class GetData:

    file_descriptor: FileDescriptor = FileDescriptor()

    def get_mac_ap(self, line):
        mac_ap = re.search('([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}):UM', line)
        return mac_ap.group(0)

    def get_mac(self, line):
        mac = re.search('([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', line)
        return mac.group(0)
        
    def get_conection_id(self, line):
        user_id = re.search('([\w\d]){16}', line)
        return user_id.group(0)

    def get_lines_by_user(self, user_id) -> list:
        lines = self.file_descriptor.read_file()
        list_lines = []
        for line in lines:
            if re.findall(user_id, line):
                list_lines.append(line)
        return list_lines

    def get_lines_by_mac_ap(self, mac_ap: str) -> list:
        lines = self.file_descriptor.read_file()
        list_lines = []
        for line in lines:
            if re.findall(mac_ap, line):
                list_lines.append(line)
        return list_lines

    def get_line_by_conection_id(self, conection_id, lines):
        for line in lines:
            if re.findall(conection_id, line):
                return line

    def get_date(self, line) -> tuple:
        dates = re.search('((\d{2}\/)+\d{4}) (\d{2}:\d{2})', line)
        # return str(dates.group(0)), str(dates.group(1))
        try:
            return str(dates.group(0)), str(dates.group(1))
        except:
            return None, None

    def get_seconds(self, line: list) -> int:
        seconds = line[4]
        return int(seconds)

    def get_trafic_down(self, line: list) -> int:
        down = line[5]
        return int(down)

    def get_trafic_up(self, line: list) -> int:
        up = line[6]
        return int(up)

    def get_start_date(self, line: list) -> str:
        start_date = line[2]
        return str(start_date)

    def get_end_date(self, line: list) -> str:
        end_date = line[3]
        return str(end_date)