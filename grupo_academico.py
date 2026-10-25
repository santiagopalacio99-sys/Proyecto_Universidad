from asignatura import Asignatura
from docente import Docente
from horario import Horario
from estudiante import Estudiante
from excepciones import EstudianteYaMatriculadoError, GrupoLlenoError, EstudianteNoMatriculadoError


class GrupoAcademico:

    def __init__(self, codigo_grupo, asignatura, docente, capacidad, horario):
        self.set_codigo_grupo(codigo_grupo)
        self.set_asignatura(asignatura)
        self.set_docente(docente)
        self.set_capacidad(capacidad)
        self.set_horario(horario)
        self._estudiantes_matriculados=[]

    def get_codigo_grupo(self):
        return self._codigo_grupo

    def get_asignatura(self):
        return self._asignatura

    def get_docente(self):
        return self._docente
    
    def get_capacidad(self):
        return self._capacidad

    def get_horario(self):
        return self._horario

    def get_estudiantes_matriculados(self):
        return self._estudiantes_matriculados

    def set_codigo_grupo(self, codigo_grupo):
        if codigo_grupo.strip() !="":
            self._codigo_grupo=(codigo_grupo)
        else:
            raise ValueError("El codigo no puede estar vacío")
        
    def set_capacidad(self, capacidad):
        if capacidad>0:
            self._capacidad=(capacidad)
        else:
            raise ValueError("La capacidad del grupo debe ser mayor a cero")

    def set_asignatura(self, asignatura):
        if isinstance(asignatura, Asignatura):
            self._asignatura= asignatura
        else:
            raise ValueError("La asignatura debe ser una Asignatura válida")

    def set_docente(self, docente):
        if isinstance(docente, Docente):
            self._docente=docente
        else:
            raise ValueError("El docente debe ser un Docente válido")

    def set_horario(self, horario):
        if isinstance(horario, Horario):
            self._horario=horario
        else:
            raise ValueError("El horario debe ser un Horario válido")

    def mostrar_informacion_grupo(self):
        print(f"codigo grupo: {self._codigo_grupo}")
        print(f"asignatura: {self._asignatura.get_nombre()}")
        print(f"docente: {self._docente.get_nombre()}")
        print(f"capacidad: {self._capacidad}")
        print(f"horario: {self._horario.get_dia()} - {self._horario.get_hora_inicio()} - {self._horario.get_hora_fin()} - {self._horario.get_salon()}")

    def matricular_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise ValueError("Debe ingresar un estudiante válido")
        if estudiante in self._estudiantes_matriculados:
            raise EstudianteYaMatriculadoError("El estudiante ya se encuentra matriculado en este grupo")
        if len(self._estudiantes_matriculados)>=self._capacidad:
            raise GrupoLlenoError ("El curso ya alcanzó su capacidad máxima")
        self._estudiantes_matriculados.append(estudiante)

    def buscar_estudiante(self, codigo_estudiantil):
        for estudiante in self._estudiantes_matriculados:
            if estudiante.get_codigo_estudiantil() == codigo_estudiantil:
                return estudiante
        return None

    def retirar_estudiante(self, codigo_estudiantil):
        estudiante = self.buscar_estudiante(codigo_estudiantil)
        if estudiante is None:
            raise EstudianteNoMatriculadoError("El estudiante no está matriculado")
        self._estudiantes_matriculados.remove(estudiante)

    def mostrar_estudiantes(self):
        if len(self._estudiantes_matriculados) == 0:
            print("No hay estudiantes registrados")
        else:
            for estudiante in self._estudiantes_matriculados:
                print(f"{estudiante.get_codigo_estudiantil()} - {estudiante.get_nombre()}")