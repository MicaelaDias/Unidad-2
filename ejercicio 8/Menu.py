from Conjunto import Conjunto
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.salir,
            
            }
    def lanzarMenu(self,conjuntoA,conjuntoB):
        #Menu opciones
        
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para unir los conjuntos.')
            print('-Ingrese 2 para diferenciar los conjuntos.')
            print('-Ingrese 3 para verificar que son iguales los conjuntos.')
            print('-Ingrese 4 para salir..')
            
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if (opcion=='1'or opcion=='2' or opcion=='3'):
                ejecutar(conjuntoA,conjuntoB)
            else:
                ejecutar()
    def opcion1(self,conjuntoA,conjuntoB):
        print('****Union de conjuntos******')
        conjuntoC=conjuntoA+conjuntoB
        conjuntoC.mostrarConjunto()
        
    def opcion2(self,conjuntoA,conjuntoB):
        print('****Diferencia de conjuntos*****')
        conjuntoD=conjuntoA-conjuntoB
        conjuntoD.mostrarConjunto()
    def opcion3(self,conjuntoA,conjuntoB):
        print('****Igualdad de conjuntos****')
        conjuntoA.mostrarConjunto()
        conjuntoB.mostrarConjunto()
        res=conjuntoA==conjuntoB
        if  res:
            print('Los conjuntos son iguales')
        else:
            print('Los conjuntos no son iguales.')
   
    def salir(self):
        print('Se cerro el menu.')
    def error(self):
        print('Opcion incorrecta.')