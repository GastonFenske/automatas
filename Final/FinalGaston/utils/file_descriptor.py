from constant import *
import re

class FileDescriptor:

    def read_file(self) -> list[str]:
        archivo = open(FILE, 'r')
        lines = archivo.readlines()
        lines.pop(0)
        archivo.close()
        return lines

    def show_line(self, line) -> list:
        line = list(re.split(r';', line))
        return line
