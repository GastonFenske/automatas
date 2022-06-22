from constant import *
from service import FileService



def show_menu() -> str: 
    print(MAIN)

# def read_option():
#     opt = int(input("Ingrese una opción: "))
#     options = {
#         # 1: show_by_user,
#         # 3: show_time_by_user,
#         # 5: Service.print_hola(),
#         5: FileService.get_macs_by_user("f10be9301bcb139a"),
#         8: FileService.order_macs_ap()
#         # 4: FileService.print_hola(),
#     }
#     return options[opt]

def read_option():
    opt = int(input("Ingrese una opción: "))
    if opt == 8:
        return FileService.get_all_mac_ap()
    elif opt == 5:
        return FileService.get_macs_by_user(input("Ingrese el usuario: "))
    elif opt == 3:
        return FileService.sesion_time(input("Ingrese el conection_id: "))
    elif opt == 1:
        return FileService.get_all_user_sessions(input("Ingrese el usuario: "))
    elif opt == 7:
        return FileService.get_trafic_by_user(input("Ingrese el usuario: "))

def main():
    show_menu()
    opt = read_option()
    print(opt)

if __name__ == '__main__':
    main()


