import csv

from PlanAhorro import PlanAhorro

class ListaDePlanes:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def agregarElementos(self,plan):
        if type(plan)==PlanAhorro:
            self.__lista.append(plan)
        else:
            print('No se puede agregar a la lista.')
    def cargarPlanes(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo,delimiter=';')       
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                PlanAhorro.setCantidadCuotasPlan(int(fila[4]))
                PlanAhorro.setCantidadCuotasParaLicitar(int(fila[5]))
                self.agregarElementos(PlanAhorro(int(fila[0]),fila[1],fila[2],float(fila[3])))
        archivo.close()
    def actualizarValor(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            valor=float(input('Ingrese el valor del vehiculo'))
            self.__lista[i].setValor(valor)
    def buscarValor(self,valor):
        for i in range(len(self.__lista)):
            if valor<self.__lista[i].valorDeCuota():
                print(self.__lista[i])
    def mostrarMonto(self):
        for i in range(len(self.__lista)):
            print('Monto que se debe pagar para licitar{}:'.format(self.__lista[i].montoParaLicitar()))
    def buscarCodigo(self,codigo):
        i=0
        bandera = False
        indice=None
        while i<len(self.__lista) and not bandera:
            if self.__lista[i].getCodigo()==codigo:
                bandera = True
                indice = i
            else:
                i+=1
        return indice 