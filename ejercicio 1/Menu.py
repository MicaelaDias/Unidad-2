import csv
import re
from Email import Email
from  ManejadorCorreo import ListaCorreo
regex= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(regex,correo):
    bandera = False
    if(re.search(regex,correo)):
        bandera = True
    return bandera
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.salir
            }
    def lanzarMenu(self,email):
        #Menu opciones
        if type(email)==Email:
            i=str(len(self.__opciones))
            opcion=0
            while(i!=opcion):
                print('Menu:')
                print('-Ingrese 1 para modificar contraseña.')
                print('-Ingrese 2 para leer un archivo y buscar dominio.')
                print('-Ingrese 3 para crear un email.')
                print('-Ingrese 4 para salir.')
                opcion=input('Ingrese opcion:\n')
                ejecutar=self.__opciones.get(opcion,self.error)
                if (opcion=='1' ):
                    ejecutar(email)
                else:
                    ejecutar()
    def opcion1(self,email):
        conActual=input('Ingresar la contraseña actual:')
        if email.verificarContrasena(conActual):
            nueva=input('ingrese la nueva contraseña:')
            email.setContrasena(nueva)
            print('Se modifico la contraseña.')
        else:
            print('Contraseña incorrecta.')
    def opcion2(self):
        manejador=ListaCorreo()
        manejador.cargarElementos()
        manejador.mostrarDatos()
        dominio=input('Ingrese el dominio que desea buscar:')
        contador=manejador.buscarDominio(dominio)
        print('La cantidad de emails con dominio {} es {}'.format(dominio,contador))
    def opcion3(self):
        emailUno=Email()
        correo=input('Ingrese la direccion de correo:')
        if (check(regex,correo)):
            contrasena=input('Ingrese la contraseña:')
            correoUno=emailUno.crearEmail(correo,contrasena)
            emailUno.crearCuenta(correoUno)
        else:
            print('direccion incorrecta')
       
    def salir(self):
        print('Se cerro el menu.')
    def error(self):
        print('Opcion incorrecta.')