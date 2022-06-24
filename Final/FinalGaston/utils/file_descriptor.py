from constant import *
import re

class FileDescriptor:

    # @staticmethod
    def read_file(self):
        archivo = open(ARCHIVO, 'r')
        lines = archivo.readlines()
        lines.pop(0)
        archivo.close()
        return lines

    # @staticmethod
    def show_line(self, line) -> list:
        line = list(re.split(r';', line))
        return line

    # @staticmethod
    def save_file(self, lines):
        archivo = open(SAFE_FILE, 'w')
        for line in lines:
            archivo.write(line)
        archivo.close()