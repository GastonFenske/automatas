import re

class GetData:

    @staticmethod
    def get_mac_ap(line):
        mac_ap = re.search('([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}):UM', line)
        return mac_ap.group(0)

    @staticmethod
    def get_mac(line):
        mac = re.search('([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', line)
        return mac.group(0)
        
    @staticmethod
    def get_conection_id(line):
        user_id = re.search('([\w\d]){16}', line)
        return user_id.group(0)

    @staticmethod
    def get_lines_by_user(user_id, lines) -> list:
        list_lines = []
        for line in lines:
            if re.findall(user_id, line):
                list_lines.append(line)
        return list_lines

    @staticmethod
    def get_line_by_conection_id(conection_id, lines):
        for line in lines:
            if re.findall(conection_id, line):
                return line

    @staticmethod
    def get_date(line):
        dates = re.search('((\d{2}\/)+\d{4}) (\d{2}:\d{2})', line)
        return dates.group(0), dates.group(1)

    @staticmethod
    def get_seconds(line: list) -> int:
        seconds = line[4]
        return int(seconds)

    @staticmethod
    def get_trafic_down(line: list) -> int:
        down = line[5]
        return int(down)

    @staticmethod
    def get_trafic_up(line: list) -> int:
        up = line[6]
        return int(up)