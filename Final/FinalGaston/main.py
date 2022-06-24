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
    file_service: FileService = FileService()
    opt = int(input("Ingrese una opción: "))
    if opt == 8:
        return file_service.order_macs_ap()
    elif opt == 5:
        return file_service.get_macs_by_user(input("Ingrese el usuario: "))
    elif opt == 3:
        return file_service.sesion_time(input("Ingrese el conection_id: "))
    elif opt == 1:
        return file_service.get_all_user_sessions(input("Ingrese el usuario: "))
    elif opt == 7:
        return file_service.get_trafic_by_user(input("Ingrese el usuario: "))
    elif opt == 2:
        return file_service.get_conection_id_by_date("28/08/2019 10:07", "csegeview")

def main():
    show_menu()
    opt = read_option()
    print(opt)

if __name__ == '__main__':
    main()


