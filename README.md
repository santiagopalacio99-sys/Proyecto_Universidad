Sistema de la comunidad académica de la universidad

Proyecto en Python que organiza la información básica de una universidad: sus personas (estudiantes, docentes y administrativos), sus programas académicos y sus asignaturas.

Integrantes
Santiago Palacio Castañeda

Descripción general del sistema

La universidad administraba estos datos en registros separados. Este sistema los reúne en un único proyecto orientado a objetos.

Persona guarda lo que todas las personas comparten: identificación, nombre y email.
Estudiante, Docente y Administrativo son tipos particulares de persona, cada uno con sus propios datos.
Empleado agrupa lo que comparten docentes y administrativos: el número de empleado.
ProgramaAcademico guarda código, nombre, facultad y número de semestres.
Asignatura guarda código, nombre, créditos y el programa académico al que pertenece.

Todos los atributos son privados (encapsulamiento). Se consultan con métodos get_... y se modifican con métodos set_..., que validan el valor y lanzan un ValueError si no es válido:

El email, la identificación, el nombre y los demás textos no pueden quedar vacíos ni contener solo espacios.
El número de semestres de un programa debe ser mayor que cero.
El número de créditos de una asignatura debe ser mayor que cero.
El semestre de un estudiante debe ser mayor que cero y su promedio debe estar entre 0 y 5.
Las horas semanales de un docente deben ser mayores que cero.
El programa de un estudiante o de una asignatura debe ser un objeto ProgramaAcademico.

Estructura de los archivos

proyecto_universidad/
├── main.py                  # Programa principal: crea objetos y ejecuta las pruebas
├── persona.py               # Clase Persona (clase base)
├── empleado.py              # Clase Empleado (hereda de Persona)
├── estudiante.py            # Clase Estudiante (hereda de Persona)
├── docente.py               # Clase Docente (hereda de Empleado)
├── administrativo.py        # Clase Administrativo (hereda de Empleado)
├── programa_academico.py    # Clase ProgramaAcademico
├── asignatura.py            # Clase Asignatura
├── docs/
│   ├── diagrama_de_clases.drawio
│   └── diagrama_de_clases.png
└── README.md

Al ejecutar, main.py demuestra:

La creación de programas académicos y una asignatura.
La creación de seis personas (dos estudiantes, dos docentes y dos administrativos) en una única lista.
La consulta de la información de los objetos.
La modificación válida de datos encapsulados (el email de un estudiante y el cargo de un administrativo).
Tres intentos de asignar valores inválidos (email vacío, semestres en 0 y créditos negativos), capturados con try / except.
La presentación particular de cada tipo de persona.
El recorrido polimórfico de la lista con un único ciclo for.
Herencia, sobreescritura y polimorfismo
Herencia

Persona es la clase base y reúne lo común: identificación, nombre, email y sus métodos. Estudiante hereda directamente de Persona. Docente y Administrativo comparten además un número de empleado, así que se creó la clase intermedia Empleado, que hereda de Persona, y de ella heredan Docente y Administrativo. De esta forma ningún atributo común se repite. Cada clase hija llama a super().__init__(...) para que el constructor de su clase madre guarde los datos generales y solo agrega lo propio.

Persona
├── Estudiante
└── Empleado
    ├── Docente
    └── Administrativo

Sobreescritura

Las clases hijas redefinen métodos de su clase madre con el mismo nombre pero con un comportamiento propio:

mostrar_informacion(): cada hija llama primero a super().mostrar_informacion() para mostrar los datos de su madre y luego imprime sus datos particulares.
realizar_actividad_principal(): en Persona muestra un mensaje general. Estudiante informa el programa que cursa y su semestre, Docente informa la facultad donde orienta clases y Administrativo informa su cargo y su dependencia.
Polimorfismo

En main.py los seis objetos viven en una sola lista y se recorren con un único ciclo for. En cada vuelta se llama a mostrar_informacion() y a realizar_actividad_principal() sin preguntar de qué tipo es el objeto: Python ejecuta automáticamente la versión que corresponde a su clase real. No hay ciclos por tipo, ni condicionales para distinguir las clases, ni llamadas manuales objeto por objeto.

for persona in personas:
    persona.mostrar_informacion()
    persona.realizar_actividad_principal()

Uso de herramientas de inteligencia artificial

Se utilizó Claude (Anthropic) como apoyo y tutor durante el desarrollo del proyecto. Su uso consistió en:

- Guiar el diseño mediante preguntas (identificación de clases, relaciones y diagrama).
- Explicar conceptos de encapsulamiento, herencia, sobreescritura y polimorfismo.
- Revisar errores del código y sugerir correcciones puntuales.

El diseño del sistema, la escritura y adaptación de las clases y las pruebas de `main.py` fueron desarrollados por mí a partir de ese acompañamiento. Revisé todo el código entregado y puedo explicarlo, justificarlo y volver a construirlo.