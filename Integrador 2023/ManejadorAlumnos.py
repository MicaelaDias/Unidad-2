import csv
import numpy as np

from Alumno import Alumno
from ManejadorMaterias import ListaMateria

class ArregloAlumnos:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    __alumnos = None

    def __init__(self,dimension=0,incremento=5):
        self.__alumnos = np.empty(dimension,dtype=Alumno)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
    def agregarAlumno(self,alumno):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad]=alumno
        self.__cantidad+=1
    def redimensionarArreglo(self):
        self.__dimension=self.__cantidad
        self.__alumnos.resize(self.__dimension)
    def cargarArchivo(self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                self.agregarAlumno(Alumno(fila[0],fila[1],fila[2],fila[3],int(fila[4])))
        archivo.close()
   
    def buscarDni(self,dni):
        i = 0
        bandera = False
        indice = None
        while i<self.__cantidad and not bandera:
            if self.__alumnos[i].getDni()==dni:
                bandera = True
                indice = i
            else:
                i+=1
        return indice
    def mostrarDatos(self,dni,fecha,nota):
        indice = self.buscarDni(dni)
        if indice!=None:
            print('{:<10}{:>15}{:>12}{:>10}{:>10}'.format(self.__alumnos[indice].getDni(),self.__alumnos[indice].getApellido()+' '+self.__alumnos[indice].getNombre(),fecha,nota,self.__alumnos[indice].getAño()))

        
    def ordenar(self):
        self.__alumnos.sort()
    def mostrarOrdenado(self):
        self.redimensionarArreglo()
        self.ordenar()
        print('{:<10}{:>15}{:>10}{:>10}'.format('DNI','Apellido y Nombre','Carrera','Año'))
        for i in range(self.__cantidad):
          print(self.__alumnos[i])