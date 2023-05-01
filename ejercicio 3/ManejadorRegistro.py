import csv

from Registro import Registro

class ListaRegistros:
    __lista = []

    def __init__(self):
        self.__lista = []
    def agregarDias(self,dias):
        for i in range(dias):
            self.__lista.append([])
    def agregarHoras(self,dia):
        for i in range(24):
            self.__lista[dia].append(None)
    def agregarElementos(self,dia,hora,registro):
        if type(registro)==Registro:
            if len(self.__lista[dia])==0:
                self.agregarHoras(dia)
            self.__lista[dia][hora]=registro
        else:
            print('No se puede agregar.')
        
    def cargarElementos(self):
        archivo = open('archivo.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                registro = Registro(int(fila[2]),int(fila[3]),int(fila[4]))
                self.agregarElementos(int(fila[0])-1,int(fila[1]),registro)
        archivo.close()
    def mayorMenorTemperatura(self):
        max = 0
        min = 99999
        diaMayorTem = 0
        horaMayorTem = 0
        diaMenorTem = 0
        horaMenorTem = 0
        for i in range(len(self.__lista)):
            for j in range(24):
                if len(self.__lista[i])!=0:
                    if self.__lista[i][j]!=None:
                        if max<self.__lista[i][j].getTemperatura():
                            max = self.__lista[i][j].getTemperatura()
                            diaMayorTem = i+1
                            horaMayorTem = j
                        if  min>self.__lista[i][j].getTemperatura():
                            min = self.__lista[i][j].getTemperatura()
                            diaMenorTem = i+1
                            horaMenorTem = j
        print('Dia {} y hora  {} de mayor temperatura'.format(diaMayorTem,horaMayorTem))
        print('Dia {} y hora {} de menor temperatura.'.format(diaMenorTem,horaMenorTem))
    def mayorMenorHumedad(self):
        max = 0
        min = 99999
        diaMayorHum = 0
        horaMayorHum = 0
        diaMenorHum = 0
        horaMenorHum = 0
        for i in range(len(self.__lista)):
            for j in range(24):
                if len(self.__lista[i])!=0:
                    if self.__lista[i][j]!=None:
                        if max<self.__lista[i][j].getHumedad():
                            max = self.__lista[i][j].getHumedad()
                            diaMayorHum = i+1
                            horaMayorHum = j
                        if  min>self.__lista[i][j].getHumedad():
                            min = self.__lista[i][j].getHumedad()
                            diaMenorHum = i+1
                            horaMenorHum = j
        print('Dia {} y hora  {} de mayor Humedad'.format(diaMayorHum,horaMayorHum))
        print('Dia {} y hora {} de menor Humedad.'.format(diaMenorHum,horaMenorHum))
    def mayorMenorPresion(self):
        max = 0
        min = 99999
        diaMayorPresion = 0
        horaMayorPresion = 0
        diaMenorPresion = 0
        horaMenorPresion = 0
        for i in range(len(self.__lista)):
            for j in range(24):
                if len(self.__lista[i])!=0:
                    if self.__lista[i][j]!=None:
                        if max<self.__lista[i][j].getPresion():
                            max = self.__lista[i][j].getPresion()
                            diaMayorPresion = i+1
                            horaMayorPresion = j
                        if  min>self.__lista[i][j].getPresion():
                            min = self.__lista[i][j].getPresion()
                            diaMenorPresion = i+1
                            horaMenorPresion = j
        print('Dia {} y hora  {} de mayor Presion'.format(diaMayorPresion,horaMayorPresion))
        print('Dia {} y hora {} de menor Presion.'.format(diaMenorPresion,horaMenorPresion))
    def calcularPromedio(self):
        acum = 0
        con = len(self.__lista)
        
        
        for i in range(len(self.__lista)):
            for  j in range(24):
                if len(self.__lista[i])!=0:
                    if self.__lista[i][j]!=None:
                        acum += self.__lista[i][j].getTemperatura()
                        
        print('La temperatura promedio mensual es {0:.2f}'.format(acum/con))
    def buscarDia(self,dia):
        cantidadDeDias=len(self.__lista)
        if dia <= cantidadDeDias:
            if self.__lista[dia]==0:
                print('No se registraron datos') 
            else:
                print('{:<10s} {:<10s} {:>14s} {:>12s}'.format('Hora','Temperatura','Humedad','Presion'))
                for j in range(len(self.__lista[dia])):
                    if self.__lista[dia][j]==None:
                        print('{:<10d} {:<10d} {:>14d} {:>12d}'.format(0,0,0,0))
                    else:
                        print('{:<10d} {:<10d} {:>14d} {:>12d}'.format(j,self.__lista[dia][j].getTemperatura(),self.__lista[dia][j].getHumedad(),self.__lista[dia][j].getPresion()))