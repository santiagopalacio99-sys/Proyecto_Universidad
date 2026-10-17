from empleado import Empleado

class Administrativo(Empleado):
    """Empleado del personal administrativo. Hereda de Empleado
    y agrega dependencia, cargo y jornada."""

    def __init__(self, identificacion, nombre, email, numero_empleado, dependencia, cargo, jornada):
        """Entrega los datos a Empleado y guarda los propios del administrativo."""
        super().__init__(identificacion,nombre,email,numero_empleado)
        self.set_dependencia(dependencia)
        self.set_cargo(cargo)
        self.set_jornada(jornada)

    def get_dependencia(self):
        """Devuelve la dependencia."""
        return self._dependencia

    def get_cargo(self):
        """Devuelve el cargo."""
        return self._cargo

    def get_jornada(self):
        """Devuelve la jornada."""
        return self._jornada

    def set_dependencia(self, nueva_dependencia):
        """Cambia la dependencia. Lanza ValueError si está vacía."""
        if nueva_dependencia.strip() !="":
            self._dependencia = nueva_dependencia
        else:
            raise ValueError("El campo dependencia no puede estar vacío")

    def set_cargo(self, nuevo_cargo):
        """Cambia el cargo. Lanza ValueError si está vacío."""
        if nuevo_cargo.strip() !="":
            self._cargo = nuevo_cargo
        else:
            raise ValueError("El campo cargo no puede estar vacío")

    def set_jornada(self, nueva_jornada):
        """Cambia la jornada. Lanza ValueError si está vacía."""
        if nueva_jornada.strip() !="":
            self._jornada = nueva_jornada
        else:
            raise ValueError("El campo jornada no puede estar vacío")

    def mostrar_informacion(self):
        """Muestra los datos de Empleado y los propios del administrativo."""
        super().mostrar_informacion()
        print(f"dependencia: {self._dependencia}")
        print(f"cargo: {self._cargo}")
        print(f"jornada: {self._jornada}")

    def realizar_actividad_principal(self):
        """Informa qué cargo desempeña y en qué dependencia trabaja."""
        print(f"El administrativo desempeña el cargo de {self._cargo} y pertenece a la dependencia {self._dependencia}")
