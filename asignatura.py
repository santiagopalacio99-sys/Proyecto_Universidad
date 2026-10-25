from programa_academico import ProgramaAcademico

class Asignatura:
    """Representa una asignatura con código, nombre, créditos
    y el programa académico al que pertenece."""

    def __init__(self, codigo, nombre, numero_creditos, programa):
        """Crea la asignatura. Cada dato pasa por su método set para validarlo."""
        self.set_codigo(codigo)
        self.set_nombre(nombre)
        self.set_numero_creditos(numero_creditos)
        self.set_programa(programa)

    def get_codigo(self):
        """Devuelve el código."""
        return self._codigo

    def get_nombre(self):
        """Devuelve el nombre."""
        return self._nombre

    def get_numero_creditos(self):
        """Devuelve el número de créditos."""
        return self._numero_creditos

    def get_programa(self):
        """Devuelve el objeto ProgramaAcademico al que pertenece."""
        return self._programa

    def set_codigo(self, codigo):
        """Cambia el código. Lanza ValueError si está vacío."""
        if codigo.strip() !="":
            self._codigo = codigo
        else:
            raise ValueError("El nuevo codigo no puede estar vacío")

    def set_nombre(self, nombre):
        """Cambia el nombre. Lanza ValueError si está vacío."""
        if nombre.strip() !="":
            self._nombre = nombre
        else:
            raise ValueError("El nuevo nombre no puede estar vacío")

    def set_numero_creditos(self, numero_creditos):
        """Cambia los créditos. Lanza ValueError si no son mayores que cero."""
        if numero_creditos > 0:
            self._numero_creditos = numero_creditos
        else:
            raise ValueError("El numero de creditos debe ser mayor a cero")

    def set_programa(self, programa):
        """Cambia el programa. Lanza ValueError si no es un objeto ProgramaAcademico."""
        if isinstance(programa, ProgramaAcademico):
            self._programa = programa
        else:
            raise ValueError("El programa debe ser un ProgramaAcademico válido")

    def mostrar_informacion(self):
        """Muestra los datos de la asignatura y el nombre de su programa."""
        print(f"codigo: {self._codigo}")
        print(f"nombre: {self._nombre}")
        print(f"numero_creditos: {self._numero_creditos}")
        print(f"programa: {self._programa.get_nombre()}")
