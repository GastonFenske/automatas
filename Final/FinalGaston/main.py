from constant import *
from service import FileService
import sys

def show_menu() -> str: 
    print(MAIN)

def read_option():
    file_service: FileService = FileService()
    opt = int(input("Ingrese una opción >>>: "))
    options = {
        1: file_service.get_all_user_sessions,
        2: file_service.get_sessions_by_user_and_date,
        6: file_service.get_users_by_macap_and_date,
        3: file_service.sesion_time,
        5: file_service.get_macs_by_user,
        7: file_service.get_trafic_by_user,
        8: file_service.order_macs_ap,
    }
    try:
        return options[opt]()
    except:
        return sys.exit()

def main():
    while True:
        show_menu()
        print(read_option())

if __name__ == '__main__':
    main()


