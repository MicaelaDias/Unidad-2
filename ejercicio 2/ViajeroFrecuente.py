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
    def cantidadTotalDeMillas(self):
        return self.__millas_acum
    def acumularMillas(self,cantidad):
        self.__millas_acum+=cantidad
        return self.__millas_acum
    def canjearMillas(self,cantidad):
        if cantidad<=self.__millas_acum:
            self.__millas_acum-=cantidad
        else:
            print('No se pueden canjear las millas.')
        return self.__millas_acum
    def mostrarDatos(self):
        return'{}, {}, {}, {}, {}'.format(self.__numero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
    def verificarNumero(self,numero):
        bandera = False
        if self.__numero==numero:
            bandera = True
        return bandera 