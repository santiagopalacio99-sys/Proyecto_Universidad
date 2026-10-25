"""Programa principal del sistema de la universidad.
Crea programas, asignaturas, personas, horarios y grupos académicos, y demuestra
el encapsulamiento, la herencia, la sobreescritura, el polimorfismo,
la clase abstracta, la composición y las excepciones personalizadas."""

from persona import Persona
from programa_academico import ProgramaAcademico
from asignatura import Asignatura
from estudiante import Estudiante
from docente import Docente
from administrativo import Administrativo
from horario import Horario
from grupo_academico import GrupoAcademico
from catalogo import Catalogo
from excepciones import (
    EstudianteYaMatriculadoError,
    GrupoLlenoError,
    EstudianteNoMatriculadoError,
    AsignaturaNoEncontradaError,
    ProgramaNoEncontradoError,
)

# ===================== ACTIVIDAD COLABORATIVA 1 =====================

sistemas = ProgramaAcademico("ISIS01", "Ingeniería de Sistemas", "Ingeniería", 10)
sistemas.mostrar_informacion()

matematicas = ProgramaAcademico("MAT08", "Matematicas", "Ciencias exactas", 9)
matematicas.mostrar_informacion()

ciberseguridad = Asignatura("AD908", "Ciberseguridad", 3, sistemas)
ciberseguridad.mostrar_informacion()

personas = [
    Estudiante("1002547491", "Santiago", "Santiago@gmail.com", "MT1234", matematicas, 4, 3.9),
    Estudiante("1006352908", "Diana", "Diana@gmail.com", "IS1945", sistemas, 9, 2.9),
    Docente("10262359", "Cristina", "Cristina@gmail.com", "0099", "Medicina", "termino indefinido", 42),
    Docente("1053859876", "Rafael", "Rafael@gmail.com", "0088", "Derecho", "Prestacion de servicios", 30),
    Administrativo("9936744", "Catalina", "Catalina@hotmail.com", "2046", "secretaría general", "Secretaria", "diurna"),
    Administrativo("68487829", "Juan", "Juan@outlook.com", "6843", "Admisiones", "Director admisiones", "nocturna"),
]

for persona in personas:
    persona.mostrar_informacion()
    persona.realizar_actividad_principal()
    print()

print("Modificación del email de Santiago:")
personas[0].set_email("palacio@gmail.com")
print(personas[0].get_email())

print("Modificación del cargo de Catalina:")
personas[4].set_cargo("Asistente rectoría")
print(personas[4].get_cargo())

print("Intento inválido 1: email vacío")
try:
    personas[0].set_email("")
except ValueError as error:
    print("Error:", error)
print("Email actual:", personas[0].get_email())

print("Intento inválido 2: semestres en 0")
try:
    sistemas.set_numero_semestres(0)
except ValueError as error:
    print("Error:", error)
print("Semestres actuales:", sistemas.get_numero_semestres())

print("Intento inválido 3: créditos negativos")
try:
    ciberseguridad.set_numero_creditos(-2)
except ValueError as error:
    print("Error:", error)
print("Créditos actuales:", ciberseguridad.get_numero_creditos())

# ===================== ACTIVIDAD COLABORATIVA 2 =====================

# Prueba 1: no se puede crear una Persona directamente
print("\n--- Prueba 1: crear una Persona directamente ---")
try:
    persona_general = Persona("1000000", "Ana", "ana@gmail.com")
except TypeError:
    print("Error: no se puede crear una persona directamente, debe ser docente, estudiante o administrativo")

# Prueba 2: creación de asignaturas, docentes, estudiantes y horarios
estudiante1 = personas[0]
estudiante2 = personas[1]
docente1 = personas[2]
docente2 = personas[3]

programacion = Asignatura("PRG01", "Programación I", 4, sistemas)

catalogo = Catalogo()
catalogo.agregar_programa(sistemas)
catalogo.agregar_programa(matematicas)
catalogo.agregar_asignatura(ciberseguridad)
catalogo.agregar_asignatura(programacion)

horario1 = Horario("Lunes", 8, 10, "Salón 203")
horario2 = Horario("Martes", 10, 12, "Salón 305")

# Prueba 3: dos grupos académicos
grupo1 = GrupoAcademico("G01", ciberseguridad, docente1, 30, horario1)
grupo2 = GrupoAcademico("G02", programacion, docente2, 1, horario2)
print("\n--- Prueba 3: grupos académicos ---")
grupo1.mostrar_informacion_grupo()
grupo2.mostrar_informacion_grupo()

# Prueba 4: matrícula correcta
print("\n--- Prueba 4: matrícula correcta ---")
grupo1.matricular_estudiante(estudiante1)
grupo1.matricular_estudiante(estudiante2)
grupo2.matricular_estudiante(estudiante1)
grupo1.mostrar_estudiantes()

# Prueba 5: estudiante duplicado
print("\n--- Prueba 5: estudiante duplicado ---")
try:
    grupo1.matricular_estudiante(estudiante1)
except EstudianteYaMatriculadoError as error:
    print("Error:", error)

# Prueba 6: superar la capacidad del grupo
print("\n--- Prueba 6: grupo lleno ---")
try:
    grupo2.matricular_estudiante(estudiante2)
except GrupoLlenoError as error:
    print("Error:", error)

# Prueba 7: retiro correcto
print("\n--- Prueba 7: retiro correcto ---")
grupo1.retirar_estudiante("IS1945")
grupo1.mostrar_estudiantes()

# Prueba 8: retirar a un estudiante que no está matriculado
print("\n--- Prueba 8: retiro de un estudiante inexistente ---")
try:
    grupo1.retirar_estudiante("IS1945")
except EstudianteNoMatriculadoError as error:
    print("Error:", error)

# Prueba 9: asignatura inexistente
print("\n--- Prueba 9: asignatura inexistente ---")
try:
    catalogo.buscar_asignatura("XYZ99")
except AsignaturaNoEncontradaError as error:
    print("Error:", error)

# Prueba 10: programa inexistente
print("\n--- Prueba 10: programa inexistente ---")
try:
    catalogo.buscar_programa("XYZ99")
except ProgramaNoEncontradoError as error:
    print("Error:", error)

# Prueba 11: el programa continúa después de controlar cada excepción
print("\nEl programa continuó su ejecución después de controlar todas las excepciones.")