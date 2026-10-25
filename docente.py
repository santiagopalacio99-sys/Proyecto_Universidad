from empleado import Empleado

class Docente(Empleado):
    """Empleado que orienta clases. Hereda de Empleado
    y agrega facultad, tipo de contrato y horas semanales."""

    def __init__(self, identificacion, nombre, email, numero_empleado, facultad, tipo_contrato, horas_semanales):
        """Entrega los datos a Empleado y guarda los propios del docente."""
        super().__init__(identificacion, nombre, email, numero_empleado)
        self.set_facultad(facultad)
        self.set_tipo_contrato(tipo_contrato)
        self.set_horas_semanales(horas_semanales)

    def get_facultad(self):
        """Devuelve la facultad."""
        return self._facultad

    def get_tipo_contrato(self):
        """Devuelve el tipo de contratación."""
        return self._tipo_contrato

    def get_horas_semanales(self):
        """Devuelve las horas semanales."""
        return self._horas_semanales

    def set_facultad(self, facultad):
        """Cambia la facultad. Lanza ValueError si está vacía."""
        if facultad.strip() !="":
            self._facultad = facultad
        else:
            raise ValueError("El campo facultad no puede estar vacío")

    def set_tipo_contrato(self, tipo_contrato):
        """Cambia el tipo de contratación. Lanza ValueError si está vacío."""
        if tipo_contrato.strip() !="":
            self._tipo_contrato = tipo_contrato
        else:
            raise ValueError("El campo contrato no puede estar vacío")

    def set_horas_semanales(self, horas_semanales):
        """Cambia las horas semanales. Lanza ValueError si no son mayores que cero."""
        if horas_semanales >0:
            self._horas_semanales = horas_semanales
        else:
            raise ValueError("Las horas semanales deben ser mayor a 0")

    def mostrar_informacion(self):
        """Muestra los datos de Empleado y los propios del docente."""
        super().mostrar_informacion()
        print(f"facultad: {self._facultad}")
        print(f"tipo_contrato: {self._tipo_contrato}")
        print(f"horas_semanales: {self._horas_semanales}")

    def realizar_actividad_principal(self):
        """Informa en qué facultad orienta clases."""
        print(f"El docente orienta clases en la facultad de: {self._facultad}")
        