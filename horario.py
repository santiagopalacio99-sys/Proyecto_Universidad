class Horario:
    """Representa cuándo y dónde se desarrolla un grupo académico:
    día, hora de inicio, hora de fin y salón."""

    def __init__(self, dia, hora_inicio, hora_fin, salon):
        """Crea el horario. Cada dato pasa por su método set para validarlo."""
        self.set_dia(dia)
        self.set_hora_inicio(hora_inicio)
        self.set_hora_fin(hora_fin)
        self.set_salon(salon)

    def get_dia(self):
        """Devuelve el día."""
        return self._dia

    def get_hora_inicio(self):
        """Devuelve la hora de inicio."""
        return self._hora_inicio

    def get_hora_fin(self):
        """Devuelve la hora de fin."""
        return self._hora_fin

    def get_salon(self):
        """Devuelve el salón."""
        return self._salon

    def set_dia(self, dia):
        """Cambia el día. Lanza ValueError si está vacío."""
        if dia.strip() !="":
            self._dia= dia
        else:
            raise ValueError("el dia no puede estar vacío")

    def set_hora_inicio(self,hora_inicio):
        """Cambia la hora de inicio. Lanza ValueError si no es mayor que cero."""
        if hora_inicio>0:
            self._hora_inicio=hora_inicio
        else:
            raise ValueError("La hora de inicio debe ser mayor a 0")
            
    def set_hora_fin(self,hora_fin):
        """Cambia la hora de fin. Lanza ValueError si no es mayor que la hora de inicio."""
        if hora_fin>self._hora_inicio:
            self._hora_fin=hora_fin
        else:
            raise ValueError("La hora de fin debe ser mayor a la hora de inicio")

    def set_salon(self, salon):
        """Cambia el salón. Lanza ValueError si está vacío."""
        if salon.strip() !="":
            self._salon = salon
        else:
            raise ValueError("El campo de salon no puede estar vacío")