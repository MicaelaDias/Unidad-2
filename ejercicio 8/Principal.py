from Conjunto import Conjunto
from Menu import Menu

if __name__=='__main__':
    conjuntoA=Conjunto()
    conjuntoB=Conjunto()
    menu=Menu()
    print('CARGAR CONJUNTOS')
    opcion=input('Ingrese los numeros para el primer conjunto y f para finalizar.')
    while opcion!='f':
        conjuntoA.agregarElementos(int(opcion))
        opcion=input('Ingrese los numeros para el primer conjunto y f para finalizar.')
        
    opcion=input('Ingrese los numeros para el segundo conjunto y f para finalizar.')
    while opcion!='f':
        conjuntoB.agregarElementos(int(opcion))
        opcion=input('Ingrese los numeros para el segundo conjunto y f para finalizar.')
    print('***Conjuntos cargados***')
    conjuntoA.mostrarConjunto()
    conjuntoB.mostrarConjunto()
    menu.lanzarMenu(conjuntoA,conjuntoB)