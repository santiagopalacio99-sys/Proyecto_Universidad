"""Programa principal del sistema de la universidad.
Crea programas, una asignatura y seis personas, y demuestra el
encapsulamiento, la herencia, la sobreescritura y el polimorfismo."""

from programa_academico import ProgramaAcademico
from asignatura import Asignatura
from estudiante import Estudiante
from docente import Docente
from administrativo import Administrativo
from persona import Persona
from horario import Horario
from grupo_academico import GrupoAcademico

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
    Administrativo("68487829", "Juan", "Juan@outlook.com", "6843", "Admisiones", "Director admisiones", "nocturna")
]

for persona in personas:
    persona.mostrar_informacion()
    persona.realizar_actividad_principal()
    print()

print("Modificación del email de Santiago:")
personas[0].set_email("palacio@gmail.com")
print(personas[0].get_email())


print("Modificacion cargo de Catalina")
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
    print("Semestre actuales:", sistemas.get_numero_semestres())

print("Intento inválido 3: créditos negativos")
try:
    ciberseguridad.set_numero_creditos(-2)
except ValueError as error:
    print("Error:", error)
    print("Créditos actuales:", ciberseguridad.get_numero_creditos())

    print("Prueba 1: crear una persona directamente")
    try:
        persona_general = persona("1000000", "Ana", "ana@gmail.com")
    except TypeError:
        print ("Error: no se puede crear una persona directamente, debe ser docente, estudiante o administrativo ")

horario_prueba = Horario("Lunes", 8, 9, "Salón 203")
print(horario_prueba.get_dia(), horario_prueba.get_hora_inicio(), horario_prueba.get_hora_fin(), horario_prueba.get_salon())

horario1 = Horario("Lunes", 8, 10, "Salón 203")
grupo1 = GrupoAcademico("G01", ciberseguridad, personas[2], 30, horario1)
grupo1.mostrar_informacion_grupo()