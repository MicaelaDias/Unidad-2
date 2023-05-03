class ViajeroFrecuente:
    __numero=0
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum=0

    def __init__(self,numero=0,dni='',nombre='',apellido='',millasAcum=0):
        self.__numero=numero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millasAcum
    def getMillas(self):
        return self.__millas_acum
    def __str__(self):
        return '{},{},{},{},{}'.format(self.__numero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
    def __eq__(self,cantidad):
        bandera = False
        if self.__millas_acum==cantidad:
            bandera=True
        return bandera
    def __req__(self,cantidad):
        bandera = False
        if self.__millas_acum==cantidad:
            bandera = True
        return bandera
    def __radd__(self,cantidad):
        return(ViajeroFrecuente(self.__numero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum+cantidad))
    def __rsub__(self,cantidad):
        resultado = None
        if cantidad<=self.__millas_acum:
            resultado = (ViajeroFrecuente(self.__numero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum-cantidad))
        else:
            resultado = (ViajeroFrecuente(self.__numero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum-cantidad))
        return resultado