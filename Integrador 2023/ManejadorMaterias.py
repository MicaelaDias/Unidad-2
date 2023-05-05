import csv

from MateriaAprobada import MateriaAprobada


class ListaMateria:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def agregarMateria(self,materia):
        if type(materia)==MateriaAprobada:
            self.__lista.append(materia)
        else:
            print('No se puede agregar el elemento.')
    def cargarArchivo(self):
        archivo = open('materiasAprobadas.csv') 
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                self.agregarMateria(MateriaAprobada(fila[0],fila[1],fila[2],int(fila[3]),fila[4]))
        archivo.close()

    def mostrarPromedios(self,dni):
        print('Promedio con aplazos:{}'.format(self.promedioConAplazos(dni)))
        print('Promedio sin aplazos:{}'.format(self.promedioSinAplazos(dni)))
        
    def promedio(self,notas,materias):
        prom = 0.0
        if materias!=0:
            prom = notas/materias
        return prom
    def promedioConAplazos(self,dni):
        acumularNota = 0
        contar = 0
        for i in range(len(self.__lista)):
            if self.__lista[i].getDni()==dni:
                
                acumularNota+=self.__lista[i].getNota()
                contar+=1
                
        promedio=self.promedio(acumularNota,contar)
        return promedio
    def promedioSinAplazos(self,dni):
        acumularNota = 0
        contar = 0
        for i in range(len(self.__lista)):
            if self.__lista[i].getDni()==dni:
                if self.__lista[i].getAprobacion()=='P' and self.__lista[i].getNota()>=7:
                    acumularNota+=self.__lista[i].getNota()
                    contar+=1
                elif self.__lista[i].getAprobacion()=='E' and  self.__lista[i].getNota()>=4:
                    acumularNota+=self.__lista[i].getNota()
                    contar+=1
                elif self.__lista[i].getAprobacion()=='X' and self.__lista[i].getNota()>=4:
                    acumularNota+=self.__lista[i].getNota()
                    contar+=1

        promedio=self.promedio(acumularNota,contar)
        return promedio
    
    def mostrarAlumnos(self,materia,manejadorAlumno):
        print('{:<10}{:>15}{:>10}{:>10}{:>10}'.format('DNI','Apellido y Nombre','Fecha','Nota','Año'))
        for i in range(len(self.__lista)):
            if self.__lista[i].getNombre()==materia:
                if self.__lista[i].getAprobacion()=='P' and self.__lista[i].getNota()>=7:
                    manejadorAlumno.mostrarDatos(self.__lista[i].getDni(),self.__lista[i].getFecha(),self.__lista[i].getNota())
                    