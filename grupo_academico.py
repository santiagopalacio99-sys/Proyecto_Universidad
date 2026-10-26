from asignatura import Asignatura
from docente import Docente
from horario import Horario
from estudiante import Estudiante
from excepciones import EstudianteYaMatriculadoError, GrupoLlenoError, EstudianteNoMatriculadoError


class GrupoAcademico:
    """Representa un grupo en el que se ofrece una asignatura. Contiene objetos
        Asignatura, Docente y Horario, y una lista de objetos Estudiante matriculados."""

    def __init__(self, codigo_grupo, asignatura, docente, capacidad, horario):
        """Crea el grupo. Los estudiantes se agregan después, con matricular_estudiante()."""
        self.set_codigo_grupo(codigo_grupo)
        self.set_asignatura(asignatura)
        self.set_docente(docente)
        self.set_capacidad(capacidad)
        self.set_horario(horario)
        self._estudiantes_matriculados=[]

    def get_codigo_grupo(self):
        """Devuelve el código del grupo."""
        return self._codigo_grupo

    def get_asignatura(self):
        """Devuelve el objeto Asignatura del grupo."""
        return self._asignatura

    def get_docente(self):
        """Devuelve el objeto Docente responsable."""
        return self._docente
    
    def get_capacidad(self):
        """Devuelve la capacidad máxima."""
        return self._capacidad

    def get_horario(self):
        """Devuelve el objeto Horario del grupo."""
        return self._horario

    def get_estudiantes_matriculados(self):
        """Devuelve la lista de estudiantes matriculados."""
        return self._estudiantes_matriculados

    def set_codigo_grupo(self, codigo_grupo):
        """Cambia el código. Lanza ValueError si está vacío."""
        if codigo_grupo.strip() !="":
            self._codigo_grupo=(codigo_grupo)
        else:
            raise ValueError("El codigo no puede estar vacío")
        
    def set_capacidad(self, capacidad):
        """Cambia la capacidad. Lanza ValueError si no es mayor que cero."""
        if capacidad>0:
            self._capacidad=(capacidad)
        else:
            raise ValueError("La capacidad del grupo debe ser mayor a cero")

    def set_asignatura(self, asignatura):
        """Cambia la asignatura. Lanza ValueError si no es un objeto Asignatura."""
        if isinstance(asignatura, Asignatura):
            self._asignatura= asignatura
        else:
            raise ValueError("La asignatura debe ser una Asignatura válida")

    def set_docente(self, docente):
        """Cambia el docente. Lanza ValueError si no es un objeto Docente."""
        if isinstance(docente, Docente):
            self._docente=docente
        else:
            raise ValueError("El docente debe ser un Docente válido")

    def set_horario(self, horario):
        """Cambia el horario. Lanza ValueError si no es un objeto Horario."""
        if isinstance(horario, Horario):
            self._horario=horario
        else:
            raise ValueError("El horario debe ser un Horario válido")

    def mostrar_informacion_grupo(self):
        """Muestra los datos del grupo, de su asignatura, de su docente y de su horario."""
        print(f"codigo grupo: {self._codigo_grupo}")
        print(f"asignatura: {self._asignatura.get_nombre()}")
        print(f"docente: {self._docente.get_nombre()}")
        print(f"capacidad: {self._capacidad}")
        print(f"horario: {self._horario.get_dia()} - {self._horario.get_hora_inicio()} - {self._horario.get_hora_fin()} - {self._horario.get_salon()}")

    def matricular_estudiante(self, estudiante):
        """Matricula a un estudiante. Lanza EstudianteYaMatriculadoError si ya está
        y GrupoLlenoError si se alcanzó la capacidad máxima."""
        if not isinstance(estudiante, Estudiante):
            raise ValueError("Debe ingresar un estudiante válido")
        if estudiante in self._estudiantes_matriculados:
            raise EstudianteYaMatriculadoError("El estudiante ya se encuentra matriculado en este grupo")
        if len(self._estudiantes_matriculados)>=self._capacidad:
            raise GrupoLlenoError ("El curso ya alcanzó su capacidad máxima")
        self._estudiantes_matriculados.append(estudiante)

    def buscar_estudiante(self, codigo_estudiantil):
        """Devuelve el estudiante matriculado con ese código, o None si no está."""
        for estudiante in self._estudiantes_matriculados:
            if estudiante.get_codigo_estudiantil() == codigo_estudiantil:
                return estudiante
        return None

    def retirar_estudiante(self, codigo_estudiantil):
        """Retira a un estudiante por su código. Lanza EstudianteNoMatriculadoError si no está."""
        estudiante = self.buscar_estudiante(codigo_estudiantil)
        if estudiante is None:
            raise EstudianteNoMatriculadoError("El estudiante no está matriculado")
        self._estudiantes_matriculados.remove(estudiante)

    def mostrar_estudiantes(self):
        """Muestra el código y el nombre de los estudiantes matriculados."""
        if len(self._estudiantes_matriculados) == 0:
            print("No hay estudiantes registrados")
        else:
            for estudiante in self._estudiantes_matriculados:
                print(f"{estudiante.get_codigo_estudiantil()} - {estudiante.get_nombre()}")