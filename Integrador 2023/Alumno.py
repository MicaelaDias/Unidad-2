class Alumno:
    __dni = ''
    __apellido = ''
    __nombre = ''
    __carrera = ''
    __año = 0

    def __init__(self,dni='',apellido='',nombre='',carrera='',año = 0):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año = año    
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getAño(self):
        return self.__año
    def __str__(self):

        return '{:<10}{:>15}{:>10}{:>10}'.format(self.__dni,self.__apellido+' '+self.__nombre,self.__carrera,self.__año)
    def __lt__(self,otro):
        res = False
        if type(otro)==Alumno:
            if self.__año<otro.getAño() and self.__apellido<otro.getApellido() and self.__nombre<otro.getNombre():
                res = True
        return res    