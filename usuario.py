from db_connection import create_connection, close_connection

class Usuario:
    def __init__(self, id, username, password):
        self.__id = id
        self.__username = username
        self.__password = password

    def usuario_menu(self):
        while True:
            print("Menú de Usuario")
            print("1. Alquilar auto")
            print("2. Devolver auto")
            print("3. Salir al Menú Principal")
            choice = input("Seleccione una opción: ")

            if choice == '1':
                placa = input("Ingrese la placa del auto que desea alquilar: ")
                self.alquilar_auto(placa)
            elif choice == '2':
                placa = input("Ingrese la placa del auto que desea devolver: ")
                self.devolver_auto(placa)
            elif choice == '3':
                break
            else:
                print("Opción no válida. Intente de nuevo")

    def alquilar_auto(self, placa):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT Estado FROM autos WHERE placa = %s", (placa,))
            auto_estado = cursor.fetchone()

            if auto_estado and auto_estado[0] == "disponible":
                cursor.execute("UPDATE autos SET Estado = 'prestado' WHERE placa = %s", (placa,))
                cursor.execute("INSERT INTO alquileres (usuario_id, placa) VALUES (%s, %s)", (self.__id, placa))
                connection.commit()
                print("Auto alquilado con éxito.")
            else:
                print("El auto no está disponible para alquilar.")

        except Exception as e:
            print("Error al alquilar el auto:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    def devolver_auto(self, placa):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT Id FROM alquileres WHERE usuario_id = %s AND placa = %s", (self.__id, placa))
            alquiler_id = cursor.fetchone()

            if alquiler_id:
                cursor.execute("UPDATE autos SET Estado = 'disponible' WHERE placa = %s", (placa,))
                cursor.execute("DELETE FROM alquileres WHERE Id = %s", (alquiler_id[0],))
                connection.commit()
                print("Auto devuelto con éxito.")
            else:
                print("El auto no está alquilado a este usuario.")

        except Exception as e:
            print("Error al devolver el auto:", str(e))

        finally:
            cursor.close()
            close_connection(connection)
