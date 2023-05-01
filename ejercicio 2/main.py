import csv

from ManejadorViajero import ListaViajeros
from Menu import  Menu

if __name__=='__main__':
    menu=Menu()
    manejador=ListaViajeros()
    manejador.cargarArchivo()
    manejador.mostrar()
    numero=int(input('Ingresar el numero de viajero: '))
    indice=manejador.buscarViajero(numero)
    if indice!=None:
        menu.lanzarMenu(manejador,indice)
    else:
        print('No se encontro el numero de viajero.')
