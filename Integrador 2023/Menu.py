from ManejadorAlumnos import ArregloAlumnos
from ManejadorMaterias import ListaMateria
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.salir
            }
    def lanzarMenu(self,manejadorAlumnos,manejadorMaterias):
        #Menu opciones
        
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para calcular promedio con y sin aplazos.')
            print('-Ingrese 2 para mostrar los alumnos aprobados.')
            print('-Ingrese 3 para mostrar ordenado por año, apellido y nombre.')
            print('-Ingrese 4 para salir.')
            
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion == '1' :
               ejecutar(manejadorMaterias)
            elif opcion=='2':
                ejecutar(manejadorAlumnos,manejadorMaterias) 
        
            elif opcion=='3':
                ejecutar(manejadorAlumnos)
            else:
                ejecutar()
    def opcion1(self,manejadorMaterias):
        dni=input('Ingrese el DNI del alumno:')
        manejadorMaterias.mostrarPromedios(dni)
        
    def opcion2(self,manejadorAlumnos,manejadorMaterias):
        nombre=input('Ingrese el nombre de la materia:')
        manejadorMaterias.mostrarAlumnos(nombre,manejadorAlumnos)

    def opcion3(self,manejadorAlumnos):
        manejadorAlumnos.mostrarOrdenado()
    
    def salir(self):
        print('Se cerro el menu.')
    def error(self):
        print('Opcion incorrecta.')