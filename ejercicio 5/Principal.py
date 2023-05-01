from ManejadorPlan import ListaDePlanes
from Menu import Menu

if __name__=='__main__':
    manejador=ListaDePlanes()
    menu=Menu()
    manejador.cargarPlanes()
    menu.lanzarMenu(manejador)