from ManejadorPlan import ListaDePlanes
from PlanAhorro import PlanAhorro
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.salir
            }
    def lanzarMenu(self,manejador):
        #Menu opciones
        if type(manejador)==ListaDePlanes:
            i=str(len(self.__opciones))
            opcion=0
            while(i!=opcion):
                print('Menu:')
                print('-Ingrese 1 para actualizar el valor de los vehiculos.')
                print('-Ingrese 2 para mostrar los vehiculos  cuya cuota es menor al valor ingresado.')
                print('-Ingrese 3 para mostrar el monto que debe pagar para licitar el vehiculo.')
                print('-Ingrese 4 para modificar la cantidad para licitar.')
                print('Ingrese 5 para salir.')
                opcion=input('Ingrese opcion:\n')
                ejecutar=self.__opciones.get(opcion,self.error)
                if (opcion=='1'or opcion=='2' or opcion=='3'):
                    ejecutar(manejador)
                else:
                    ejecutar()
    def opcion1(self,manejador):
        manejador.actualizarValor()
        
    def opcion2(self,manejador):
       valor = float(input('Ingrese el valor del vehiculo:'))
       manejador.buscarValor(valor)
       
    def opcion3(self,manejador):
       manejador.mostrarMonto()
    def opcion4(self):
        cuota=int(input('Ingrese la cantidad de cuotas para licitar'))
        PlanAhorro.setCantidadCuotasParaLicitar(cuota)
    def salir(self):
        print('Se cerro el menu.')
    def error(self):
        print('Opcion incorrecta.')