from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes = None):
        if asignaturas == None:
            asignaturas = []
        if estudiantes == None:
            estudiantes = []
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista = None):
        if lista == None:
            lista = []
        lista.append(alumno)
        for alumno in lista:
            self.listadoAlumnos.append (alumno)
    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo


    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
