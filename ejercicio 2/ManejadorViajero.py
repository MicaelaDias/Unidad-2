import csv
from ViajeroFrecuente import ViajeroFrecuente

class ListaViajeros:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def agregarElementos(self,viajero):
        if type(viajero)==ViajeroFrecuente:
            self.__lista.append(viajero)
        else:
            print('No se puede agregar.')
    def cargarArchivo(self):
        archivo=open('archivo.csv')
        reader=csv.reader(archivo,delimiter=',')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                self.agregarElementos(ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4])))
        archivo.close()
    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i].mostrarDatos())
    def buscarViajero(self,numero):
        bandera = False
        indice=None
        i=0
        cantidad=len(self.__lista)
        while not bandera and i<cantidad:
            if self.__lista[i].verificarNumero(numero):
                bandera = True
                indice=i

            else:
                i+=1
        return indice
    def consultarMillas(self,indice):
        print('La cantidad de millas acumuladas es {}'.format(self.__lista[indice].cantidadTotalDeMillas()))
    def acumularMillas(self,indice,cantidad):
        print('Cantidad de millas actualizadas {}'.format(self.__lista[indice].acumularMillas(cantidad)))
    def canjearMillas(self,indice,cantidad):
        print('Cantidad total de millas {}'.format(self.__lista[indice].canjearMillas(cantidad)))