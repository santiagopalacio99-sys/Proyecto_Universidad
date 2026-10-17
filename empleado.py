from persona import Persona

class Empleado(Persona):
    """Persona que trabaja en la universidad. Hereda de Persona
    y agrega el número de empleado, común a docentes y administrativos."""


    def __init__(self, identificacion, nombre, email, numero_empleado):
        """Entrega los datos generales a Persona y guarda el número de empleado."""
        super().__init__(identificacion, nombre, email)
        self.set_numero_empleado(numero_empleado)

    def get_numero_empleado(self):
        """Devuelve el número de empleado."""
        return self._numero_empleado

    def set_numero_empleado(self, nuevo_numero_empleado):
        """Cambia el número de empleado. Lanza ValueError si está vacío."""
        if nuevo_numero_empleado.strip() !="":
            self._numero_empleado = nuevo_numero_empleado
        else:
            raise ValueError("El nuevo numero de empleado no puede estar vacío")

    def mostrar_informacion(self):
        """Muestra los datos de Persona y el número de empleado."""
        super().mostrar_informacion()
        print(f"numero_empleado: {self._numero_empleado}")