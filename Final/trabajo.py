
FILE = 'UsuariosWiFi.txt'

lineas: list = []
def read_file():
    with open(FILE) as f:
        for line in f:
            lineas.append(line)
        return lineas

def count_lines(lines):
    num = 0
    for line in lines:
        if len(line) != 9:
            print(line, f'[{num}]')
        num += 1

def main():
    count_lines(read_file())

if __name__ == '__main__':
    main()

