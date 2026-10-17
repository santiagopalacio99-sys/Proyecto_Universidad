from persona import Persona
from programa_academico import ProgramaAcademico

class Estudiante(Persona):
    """Persona matriculada en un programa académico.
    Hereda de Persona y agrega código, programa, semestre y promedio."""


    def __init__(self, identificacion, nombre, email, codigo_estudiantil, programa, semestre, promedio_acumulado):
        """Entrega los datos generales a Persona y guarda los propios del estudiante."""
        super().__init__(identificacion, nombre, email)
        self.set_codigo_estudiantil(codigo_estudiantil)
        self.set_programa(programa)
        self.set_semestre(semestre)
        self.set_promedio_acumulado(promedio_acumulado)

    def get_codigo_estudiantil(self):
        """Devuelve el código estudiantil."""
        return self._codigo_estudiantil

    def get_programa(self):
        """Devuelve el objeto ProgramaAcademico del estudiante."""
        return self._programa

    def get_semestre(self):
        """Devuelve el semestre."""
        return self._semestre

    def get_promedio_acumulado(self):
        """Devuelve el promedio acumulado."""
        return self._promedio_acumulado

    def set_codigo_estudiantil(self, nuevo_codigo_estudiantil):
        """Cambia el codigo de estudiante. Lanza ValueError si está vacío."""
        if nuevo_codigo_estudiantil.strip() !="":
            self._codigo_estudiantil = nuevo_codigo_estudiantil
        else:
            raise ValueError("El codigo estudiantil no puede estar vacío")

    def set_programa(self, nuevo_programa):
        """Cambia el programa. Lanza ValueError si no es un objeto ProgramaAcademico."""
        if isinstance(nuevo_programa, ProgramaAcademico):
            self._programa = nuevo_programa
        else:
            raise ValueError("Debe ingresar un programa académico válido")

    def set_semestre(self, nuevo_semestre):
        """Cambia el semestre. Lanza ValueError si no es mayor que cero."""
        if nuevo_semestre >0:
            self._semestre = nuevo_semestre
        else:
            raise ValueError("ingrese un semestre válido")

    def set_promedio_acumulado(self, nuevo_promedio_acumulado):
        """Cambia el promedio. Lanza ValueError si no está entre 0 y 5."""
        if 0<= nuevo_promedio_acumulado <=5:
            self._promedio_acumulado = nuevo_promedio_acumulado
        else:
            raise ValueError("el nuevo promedio debe estar entre 0 y 5")

    def mostrar_informacion(self):
        """Muestra los datos de Persona y los propios del estudiante."""
        super().mostrar_informacion()
        print(f"codigo_estudiantil: {self._codigo_estudiantil}")
        print(f"programa: {self._programa.get_nombre()}")
        print(f"semestre: {self._semestre}")
        print(f"promedio_acumulado: {self._promedio_acumulado}")

    def realizar_actividad_principal(self):
        """Informa qué programa cursa y en qué semestre está."""
        print(f"El estudiante cursa {self._programa.get_nombre()} y está en el semestre {self._semestre}")



    
        
    