from excepciones import AsignaturaNoEncontradaError, ProgramaNoEncontradoError

class Catalogo:

    def __init__(self):
        self._asignaturas = []
        self._programas = []

    def agregar_asignatura(self, asignatura):
        self._asignaturas.append(asignatura)

    def agregar_programa(self, programa):
        self._programas.append(programa)

    def buscar_asignatura(self, codigo):
        for asignatura in self._asignaturas:
            if asignatura.get_codigo()==codigo:
                return asignatura
        raise AsignaturaNoEncontradaError(f"No existe una asigntura con el código {codigo}")

    def buscar_programa(self, codigo):
        for programa in self._programas:
            if programa.get_codigo()==codigo:
                return programa
            raise ProgramaNoEncontradoError(f"No existe ningun programa con el código {codigo}")