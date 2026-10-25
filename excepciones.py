class EstudianteYaMatriculadoError(Exception):
    """Se lanza cuando se intenta matricular a un estudiante que ya está en el grupo."""
    pass


class GrupoLlenoError(Exception):
    """Se lanza cuando el grupo alcanzó su capacidad máxima."""
    pass


class EstudianteNoMatriculadoError(Exception):
    """Se lanza cuando se intenta retirar a un estudiante que no está en el grupo."""
    pass


class AsignaturaNoEncontradaError(Exception):
    """Se lanza cuando se busca una asignatura que no existe."""
    pass


class ProgramaNoEncontradoError(Exception):
    """Se lanza cuando se busca un programa académico que no existe."""
    pass