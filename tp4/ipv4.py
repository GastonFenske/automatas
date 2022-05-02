import re

NOMBRE_ARCHIVO = 'ipv4s.txt'
PATRON = '^((25[0-5]|000|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$'

class Analizador:

    def leer_archivo(self):
        file = open(NOMBRE_ARCHIVO, 'r')
        lines = file.readlines()
        return lines

    def formatear_lineas(self, lineas: list):
        lines = [line[:-1] for line in lineas if line is not lineas[-1]]
        lines.append(lineas[-1])
        return lines

    def comprobar_linea(self, linea: str) -> bool:
        return True if re.fullmatch(PATRON, linea) else False

    def recorrer_archivo(self) -> None:
        for line in self.formatear_lineas(self.leer_archivo()):
            if self.comprobar_linea(str(line)):
                print(f'La linea ({line}) SI es una ipv4 valida')
            else:
                print(f'La linea ({line}) NO es una ipv4 valida')

def main() -> None:
    analizador = Analizador()
    analizador.recorrer_archivo()

if __name__ == '__main__':
    main()