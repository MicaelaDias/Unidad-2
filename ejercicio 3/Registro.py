class Registro:
    __temperatura = 0 
    __humedad = 0
    __presion = 0
    def __init__(self,temperatura=0,humedad=0,presion=0):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion
    def getTemperatura(self):
        return self.__temperatura
    def getHumedad(self):
        return self.__humedad
    def getPresion(self):
        return self.__presion