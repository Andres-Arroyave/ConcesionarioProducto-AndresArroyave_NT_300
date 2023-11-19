from concesionario import Concesionario
from asesor import Asesor
from usuario import Usuario

def main():
    print("Bienvenido al concesionario")

    while True:
        print("Menú Principal")
        print("1. Registro")
        print("2. Iniciar Sesión")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            username = input("Ingrese su nombre de usuario: ")
            rol = input("Ingrese su rol (asesor/usuario): ")
            password = input("Digite su contraseña: ")

            id = 0

            Concesionario.register(id, username, rol, password)
            print("Registro exitoso")
        elif choice == '2':
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            user_id, username, rol = Concesionario.login(username, password)
            if rol == 'asesor':
                Asesor(id=user_id, username=username, password=password).asesor_menu()
            elif rol == 'usuario':
                Usuario(id=user_id, username=username, password=password).usuario_menu()
        elif choice == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
