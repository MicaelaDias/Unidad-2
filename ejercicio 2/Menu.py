from ViajeroFrecuente import ViajeroFrecuente
from ManejadorViajero import ListaViajeros
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.salir
            }
    def lanzarMenu(self,manejador,indice):
        #Menu opciones
        if type(manejador)==ListaViajeros:
            i=str(len(self.__opciones))
            opcion=0
            while(i!=opcion):
                print('Menu:')
                print('-Ingrese 1 para consultar millas.')
                print('-Ingrese 2 para acumular millas.')
                print('-Ingrese 3 para la canjear millas.')
                print('-Ingrese 4 para salir.')
                opcion=input('Ingrese opcion:\n')
                ejecutar=self.__opciones.get(opcion,self.error)
                if (opcion=='1'or opcion=='2' or opcion=='3' ):
                    ejecutar(manejador,indice)
                else:
                    ejecutar()
    def opcion1(self,manejador,indice):
        manejador.consultarMillas(indice)
    def opcion2(self,manejador,indice):
        cantidad=int(input('Ingrese la cantdad de millas:'))
        manejador.acumularMillas(indice,cantidad)
    def opcion3(self,manejador,indice):
        cantidad=int(input('Ingrese la cantidad de millas para canjear:'))
        manejador.canjearMillas(indice,cantidad)
        
    def salir(self):
        print('Se cerro el menu.')
    def error(self):
        print('Opcion incorrecta.')