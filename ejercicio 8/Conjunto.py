class Conjunto:
    __conjunto=[]

    def __init__(self):
        self.__conjunto=[]
    def agregarElementos(self,numero):
        if type(numero)==int:
            if not numero in self.__conjunto:
                self.__conjunto.append(numero)
        else:
            print('No se puede agregar el elemento.')
    def mostrarConjunto(self):
        print(self.__conjunto)
    def cargarConjuntoC(self,conjuntoC):
        for numero in self.__conjunto:
            conjuntoC.agregarElementos(numero)
       
    def __add__(self,conjuntoB):
        conjuntoC=Conjunto()
        self.cargarConjuntoC(conjuntoC)
        conjuntoB.cargarConjuntoC(conjuntoC)
        return conjuntoC
    def verificarValor(self,numero):
        return numero in self.__conjunto
        
    def cargarConjuntoD(self,conjuntoD,conjuntoB):
        for numero in self.__conjunto:
            if not conjuntoB.verificarValor(numero):
                conjuntoD.agregarElementos(numero)
    def __sub__(self,conjuntoB):
        conjuntoD=Conjunto()
        self.cargarConjuntoD(conjuntoD,conjuntoB)
        return conjuntoD
    def verificarLongitud(self):
        longitud = len(self.__conjunto)
        return longitud
    def __eq__(self,conjuntoB):
        bandera = True
        i = 0
        res = False
        longitudConjuntoA=len(self.__conjunto)
        if longitudConjuntoA==conjuntoB.verificarLongitud():
            while i<longitudConjuntoA and bandera:
                if conjuntoB.verificarValor(self.__conjunto[i]):
                    i+=1
                else:
                    bandera = False
            if bandera:
                res = True
        return res