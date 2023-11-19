from db_connection import create_connection, close_connection

class Asesor:
    def __init__(self, id, username, password):
        self.__id = id
        self.__username = username
        self.__password = password

    def asesor_menu(self):
        while True:
            print("Menú de Asesor")
            print("1. Registrar auto")
            print("2. Listar autos")
            print("3. Listar alquileres")
            print("4. Salir al Menú Principal")
            choice = input("Seleccione una opción: ")

            if choice == '1':
                self.add_auto()
            elif choice == '2':
                self.list_autos()
            elif choice == '3':
                self.list_alquileres()
            elif choice == '4':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def add_auto(self):
        placa = input("Placa del auto: ")
        referencia = input("Referencia del auto: ")
        marca = input("Marca del auto: ")
        estado = input("Estado del auto (disponible/prestado): ")

        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO autos (placa, Referencia, Marca, Estado) VALUES (%s, %s, %s, %s)",
                           (placa, referencia, marca, estado))
            connection.commit()
            print(f"Auto registrado exitosamente: Placa {placa}, Referencia {referencia}")

        except Exception as e:
            print("Error al registrar el auto:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    def list_autos(self):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT placa, Referencia, Marca, Estado FROM autos")
            autos = cursor.fetchall()

            if autos:
                print("Lista de autos:")
                for auto in autos:
                    placa, referencia, marca, estado = auto
                    print(f"Placa: {placa}, Referencia: {referencia}, Marca: {marca}, Estado: {estado}")
            else:
                print("No hay autos registrados en la base de datos.")

        except Exception as e:
            print("Error al listar autos:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    def list_alquileres(self):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT Id, usuario_id, placa, fecha_alquiler, fecha_devolucion FROM alquileres")
            alquileres = cursor.fetchall()

            if alquileres:
                print("Lista de alquileres:")
                for alquiler in alquileres:
                    alquiler_id, usuario_id, placa, fecha_alquiler, fecha_devolucion = alquiler
                    print(f"ID Alquiler: {alquiler_id}, ID Usuario: {usuario_id}, Placa del auto: {placa}, Fecha alquiler: {fecha_alquiler}, Fecha devolución: {fecha_devolucion}")
            else:
                print("No hay alquileres registrados en la base de datos.")

        except Exception as e:
            print("Error al listar alquileres:", str(e))

        finally:
            cursor.close()
            close_connection(connection)
