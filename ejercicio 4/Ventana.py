class Ventana:
    __titulo = ''
    __xSupIzquierdo = 0
    __ySupizquierdo = 0
    __xInfDerecho = 0
    __yInfDerecho = 0

    def __init__(self,titulo='', xSupIzquierdo = 0, ySupIzquierdo=0, xInfDerecho = 500, yInfDerecho = 500):
        self.__titulo = titulo
        self.__xSupIzquierdo = xSupIzquierdo
        self .__ySupizquierdo = ySupIzquierdo
        self.__xInfDerecho = xInfDerecho
        self.__yInfDerecho = yInfDerecho
    def mostrar(self):
        print('titulo: {}, Vertice superior izquierdo:<{},{}>, Vertice inferior derecho:<{},{}>'.format(self.__titulo,self.__xSupIzquierdo,self.__ySupizquierdo,self.__xInfDerecho,self.__yInfDerecho))
    def alto(self):
        return self.__yInfDerecho - self.__ySupizquierdo
    def ancho(self):
        return self.__xInfDerecho - self.__xSupIzquierdo
    def getTitulo(self):
        return self.__titulo
    def moverDerecha(self,desp=1):
       if self.__xSupIzquierdo<self.__xInfDerecho:
            desplazamiento=self.__xInfDerecho+desp
            if desplazamiento<=500:
                desplazamientoDos=self.__xSupIzquierdo+desp
                self.__xSupIzquierdo=desplazamientoDos
                self.__xInfDerecho=desplazamiento
                
            else:
                print('No se puede realizar la operacion')
    def moverIzquierda(self,desp=1):
        if self.__xSupIzquierdo<self.__xInfDerecho:
            desplazamiento=self.__xSupIzquierdo-desp
            if desplazamiento>=0:
                desplazamientoDos=self.__xInfDerecho-desp
                self.__xSupIzquierdo=desplazamiento
                self.__xInfDerecho=desplazamientoDos
                
            else:
                print('No se puede realizar la operacion')
    def bajar(self,desp=1):
        if self.__ySupizquierdo<self.__yInfDerecho:
            desplazamiento=self.__ySupizquierdo-desp
            if desplazamiento>=0:
                desplazamientoDos=self.__yInfDerecho-desp
                self.__yInfDerecho=desplazamientoDos
                self.__ySupizquierdo=desplazamiento

            else:
                print('No se puede realizar la operacion')
    def subir(self,desp=1):
        if self.__ySupizquierdo<self.__yInfDerecho:
            desplazamiento=self.__yInfDerecho+desp
            if desplazamiento<=500:
                desplazamientoDos=self.__ySupizquierdo+desp
                self.__ySupizquierdo=desplazamientoDos
                self.__yInfDerecho=desplazamiento
            else:
                print('No se puede realizar la operacion')

    

        
        