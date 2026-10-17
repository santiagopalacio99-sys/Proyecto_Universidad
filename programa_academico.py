class ProgramaAcademico:
    """Representa un programa académico con código, nombre,
    facultad y número de semestres."""

    def __init__(self, codigo, nombre, facultad, numero_semestres):
        """Crea el programa. Cada dato pasa por su método set para validarlo."""
        self.set_codigo(codigo)
        self.set_nombre(nombre)
        self.set_facultad(facultad)
        self.set_numero_semestres(numero_semestres)

    def get_codigo(self):
        """Devuelve el código."""
        return self._codigo

    def get_nombre(self):
        """Devuelve el nombre."""
        return self._nombre

    def get_facultad(self):
        """Devuelve la facultad."""
        return self._facultad

    def get_numero_semestres(self):
        """Devuelve el número de semestres."""
        return self._numero_semestres

    def set_codigo(self, nuevo_codigo):
        """Cambia el código. Lanza ValueError si está vacío."""
        if nuevo_codigo.strip() != "":
            self._codigo = nuevo_codigo
        else:
            raise ValueError("El codigo no puede quedar vacío")

    def set_nombre(self, nuevo_nombre):
        """Cambia el nombre. Lanza ValueError si está vacío."""
        if nuevo_nombre.strip() != "":
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre no puede quedar vacío")

    def set_facultad(self, nueva_facultad):
        """Cambia la facultad. Lanza ValueError si está vacía."""
        if nueva_facultad.strip() != "":
            self._facultad = nueva_facultad
        else:
            raise ValueError("La facultad no puede quedar vacía")

    def set_numero_semestres(self, nuevo_numero_semestres):
        """Cambia los semestres. Lanza ValueError si no son mayores que cero."""
        if nuevo_numero_semestres > 0:
            self._numero_semestres = nuevo_numero_semestres
        else:
            raise ValueError("Los semestres deben ser mayores a 0")

    def mostrar_informacion(self):
        """Muestra los cuatro datos principales del programa."""
        print(f"codigo: {self._codigo}")
        print(f"nombre: {self._nombre}")
        print(f"facultad: {self._facultad}")
        print(f"numero_semestres: {self._numero_semestres}")