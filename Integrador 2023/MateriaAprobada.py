class MateriaAprobada:
    __dni = ''
    __nombreDeMateria = ''
    __fecha = ''
    __nota = 0
    __aprobacion = ''

    def __init__(self,dni='',nombre='',fecha='',nota=0,aprobacion=''):
        self.__dni = dni
        self.__nombreDeMateria = nombre
        self.__fecha = fecha
        self.__nota=nota
        self.__aprobacion = aprobacion
    def getDni(self):
        return self.__dni
    def getNota(self):
        return self.__nota
    def getNombre(self):
        return self.__nombreDeMateria
    def getFecha(self):
        return self.__fecha
    def getAprobacion(self):
        return self.__aprobacion