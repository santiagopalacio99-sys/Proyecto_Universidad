from abc import ABC, abstractclassmethod

class Persona(ABC):
    """Representa a una persona vinculada a la universidad.
    Guarda identificación, nombre y email como atributos privados."""

    def __init__(self, identificacion, nombre, email):
        """Crea una persona. Cada dato pasa por su método set para validarlo."""
        self.set_identificacion(identificacion)
        self.set_nombre(nombre)
        self.set_email(email)

    def get_identificacion(self):
        """Devuelve la identificación."""
        return self._identificacion

    def get_nombre(self):
        """Devuelve el nombre."""
        return self._nombre

    def get_email(self):
        """Devuelve el email."""
        return self._email

    def set_identificacion(self, nueva_identificacion):
        """Cambia la identificación. Lanza ValueError si está vacía."""
        if nueva_identificacion.strip() != "":
            self._identificacion = nueva_identificacion
        else:
            raise ValueError("La identificacion no puede quedar vacía")

    def set_nombre(self, nuevo_nombre):
        """Cambia el nombre. Lanza ValueError si está vacío."""
        if nuevo_nombre.strip() != "":
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre no puede quedar vacío")

    def set_email(self, nuevo_email):
        """Cambia el email. Lanza ValueError si está vacío o solo tiene espacios."""
        if nuevo_email.strip() != "":
            self._email = nuevo_email
        else:
            raise ValueError("El email no puede quedar vacío")

    def mostrar_informacion(self):
        """Muestra la identificación, el nombre y el email."""
        print(f"identificacion: {self._identificacion}")
        print(f"nombre: {self._nombre}")
        print(f"email: {self._email}")

    def realizar_actividad_principal(self):
        """Método abstracto: cada clase especializada define su actividad principal."""
        pass