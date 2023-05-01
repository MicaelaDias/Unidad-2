from ManejadorRegistro import ListaRegistros
from Menu import Menu

if __name__=='__main__':
    manejador = ListaRegistros()
    
    dias = int(input('Ingrese la cantidad de dias'))
    if dias<1:
        print('no valido.')
    else:
        manejador.agregarDias(dias)
        manejador.cargarElementos()
        menu = Menu()
        menu.lanzarMenu(manejador)
