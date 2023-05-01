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
    
    def mayor(self):
        max=0
        for i in range(len(self.__lista)):
            if self.__lista[i]>self.__lista[max]:
                max = i
        return max
    def mostrarMayor(self,indice):
        for i in range(len(self.__lista)):
            if self.__lista[i]==self.__lista[indice]:
                print(self.__lista[i])