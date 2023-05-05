from ManejadorAlumnos import ArregloAlumnos
from ManejadorMaterias import ListaMateria
from Menu import Menu

if __name__=='__main__':
    manejadorAlumnos = ArregloAlumnos()
    manejadorMaterias = ListaMateria()
    menu = Menu()
    manejadorAlumnos.cargarArchivo()
    manejadorMaterias.cargarArchivo()
    menu.lanzarMenu(manejadorAlumnos,manejadorMaterias)