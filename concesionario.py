from db_connection import create_connection, close_connection


class Concesionario:
    def __init__(self):
        self.__id = None
        self.__username = None
        self.__rol = None
        self.__password = None

    @staticmethod
    def register(id, username, rol, password):
        connection = create_connection()
        if not connection:
            return
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO Usuarios (id, username, rol, password) VALUES (%s, %s, %s, %s)",
                           (id, username, rol, password))
            connection.commit()
            print("Usuario registrado exitosamente.")

        except Exception as e:
            print("Error al registrar usuario:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    @staticmethod
    def login(username, password):
        connection = create_connection()
        if not connection:
            return
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT id, rol FROM Usuarios WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()

            if user:
                id, rol = user
                print(f"Bienvenido, {username} ({rol}).")
                return id, username, rol
            else:
                print("Credenciales incorrectas. Por favor, intenta de nuevo.")

        except Exception as e:
            print("Error al iniciar sesión:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    @staticmethod
    def add_car(placa, referencia, marca, estado):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO Autos (placa, Referencia, Marca, Estado) VALUES (%s, %s, %s, %s)",
                           (placa, referencia, marca, estado))
            connection.commit()
            print(f"Auto registrado exitosamente: Placa {placa}, Referencia {referencia}")

        except Exception as e:
            print("Error al registrar el auto:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    @staticmethod
    def list_cars():
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT Placa, Referencia, Marca, Estado FROM Autos")
            cars = cursor.fetchall()

            if cars:
                print("Lista de autos:")
                for car in cars:
                    placa, referencia, marca, estado = car
                    print(f"Placa: {placa}, Referencia: {referencia}, Marca: {marca}, Estado: {estado}")
            else:
                print("No hay autos registrados en la base de datos.")

        except Exception as e:
            print("Error al listar autos:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    @staticmethod
    def list_rented_cars():
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT p.id, a.placa, a.referencia, a.marca FROM Alquileres p "
                           "INNER JOIN Autos a ON p.placa = a.placa")
            rents = cursor.fetchall()

            if rents:
                print("Lista de autos alquilados:")
                for rent in rents:
                    rent_id, car_placa, car_referencia, car_marca = rent
                    print(
                        f"Alquiler ID: {rent_id}, Placa del auto: {car_placa}, Referencia: {car_referencia}, Marca: {car_marca}")
            else:
                print("No hay autos alquilados registrados en la base de datos.")

        except Exception as e:
            print("Error al listar autos alquilados:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    @staticmethod
    def rent_car(user_id, car_placa):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT Estado FROM Autos WHERE placa = %s", (car_placa,))
            car_status = cursor.fetchone()

            if car_status and car_status[0] == "disponible":
                cursor.execute("UPDATE Autos SET Estado = 'alquilado' WHERE placa = %s", (car_placa,))
                cursor.execute("INSERT INTO Alquileres (usuario_id, placa, fecha_alquiler) VALUES (%s, %s, NOW())",
                               (user_id, car_placa))
                connection.commit()
                print("Auto alquilado con éxito.")
            else:
                print("El auto no está disponible para alquilar.")

        except Exception as e:
            print("Error al alquilar el auto:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    @staticmethod
    def return_car(user_id, car_placa):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT id FROM Alquileres WHERE usuario_id = %s AND auto_placa = %s", (user_id, car_placa))
            rent_id = cursor.fetchone()

            if rent_id:
                cursor.execute("UPDATE Autos SET Estado = 'disponible' WHERE placa = %s", (car_placa,))
                cursor.execute("DELETE FROM Alquileres WHERE id = %s", (rent_id[0],))
                connection.commit()
                print("Auto devuelto con éxito.")
            else:
                print("El auto no está alquilado por este usuario.")

        except Exception as e:
            print("Error al devolver el auto:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def rol(self):
        return self.__rol

    @rol.setter
    def rol(self, rol):
        self.__rol = rol

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
