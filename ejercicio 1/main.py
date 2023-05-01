import csv
from Email import Email
from ManejadorCorreo import ListaCorreo
from Menu import Menu

if __name__=='__main__':
   
    
    #punto 1
    nombre=input('Ingrese su nombre:')
    idCuenta=input('Ingrese el identificador de cuenta:')
    dominio=input('Ingrese el dominio de su email:')
    tipo=input('Ingrese el tipo de dominio:')
    contrasena=input('Ingrese la contraseña:')
    email=Email(idCuenta,dominio,tipo,contrasena)
    print('Estimado {} te enviaremos tus mensajes a la direccion {}'.format(nombre,email.retornaEmail()))
    menu=Menu()
    menu.lanzarMenu(email)