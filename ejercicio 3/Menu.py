from ManejadorRegistro import ListaRegistros
from  Registro import Registro
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.salir
            }
    def lanzarMenu(self,manejador):
        #Menu opciones
        if type(manejador)==ListaRegistros:
            i=str(len(self.__opciones))
            opcion=0
            while(i!=opcion):
                print('Menu:')
                print('-Ingrese 1 para consultar mayor y menor valor.')
                print('-Ingrese 2 para consultar la temperatura promedio mensual.')
                print('-Ingrese 3 para consultar las variables metereológicas.')
                print('-Ingrese 4 para salir.')
                opcion=input('Ingrese opcion:\n')
                ejecutar=self.__opciones.get(opcion,self.error)
                if (opcion=='1'or opcion=='2' or opcion=='3' ):
                    ejecutar(manejador)
                else:
                    ejecutar()
    def opcion1(self,manejador):
        manejador.mayorMenorTemperatura()
        manejador.mayorMenorHumedad()
        manejador.mayorMenorPresion()
    def opcion2(self,manejador):
       manejador.calcularPromedio()
    def opcion3(self,manejador):
        dia=int(input('Ingrese el numero del dia'))
        manejador.buscarDia(dia-1)
    def salir(self):
        print('Se cerro el menu.')
    def error(self):
        print('Opcion incorrecta.')