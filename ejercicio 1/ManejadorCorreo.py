import csv
import re
from Email import Email 


class ListaCorreo:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def agregarElemento(self,correo):
        if type(correo)==Email:
            self.__lista.append(correo)
        else:
            print('No es un Email, no se puede agregar.')
    def cargarElementos(self):
        lineaCompleta=None
        archivo=open('archivo.csv')
        reader=csv.reader(archivo,delimiter=',')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                self.agregarElemento(Email(fila[0],fila[1],fila[2],fila[3]))
                
                    
        archivo.close()
    def mostrarDatos(self):
        for i in range(len(self.__lista)):
            print('email:{}'.format(self.__lista[i].retornaEmail()))
    def buscarDominio(self,dominio):
        contar=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getDominio()==dominio:
                contar+=1
        return contar