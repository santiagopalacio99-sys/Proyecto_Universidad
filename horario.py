class Horario:

    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.set_dia(dia)
        self.set_hora_inicio(hora_inicio)
        self.set_hora_fin(hora_fin)
        self.set_salon(salon)

    def get_dia(self):
        return self._dia

    def get_hora_inicio(self):
        return self._hora_inicio

    def get_hora_fin(self):
        return self._hora_fin

    def get_salon(self):
        return self._salon

    def set_dia(self, dia):
        if dia.strip() !="":
            self._dia= dia
        else:
            raise ValueError("el dia no puede estar vacío")

    def set_hora_inicio(self,hora_inicio):
        if hora_inicio>0:
            self._hora_inicio=hora_inicio
        else:
            raise ValueError("La hora de inicio debe ser mayor a 0")
            
    def set_hora_fin(self,hora_fin):
        if hora_fin>self._hora_inicio:
            self._hora_fin=hora_fin
        else:
            raise ValueError("La hora de fin debe ser mayor a la hora de inicio")

    def set_salon(self, salon):
        if salon.strip() !="":
            self._salon = salon
        else:
            raise ValueError("El campo de salon no puede estar vacío")