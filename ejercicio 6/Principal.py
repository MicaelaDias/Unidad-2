from ViajeroFrecuente import ViajeroFrecuente
from ManejadorViajero import ListaViajeros
if __name__=='__main__':
    manejador=ListaViajeros()
    manejador.cargarArchivo()
    viajero=ViajeroFrecuente(230,'42335678','Carlos','Cortez',400)
    print('***Viajero con mayor cantidad de millas***')
    indice=manejador.mayor()
    manejador.mostrarMayor(indice)
    print('***Acumular millas***')
    viajeroUno=viajero+100
    print(viajeroUno)
    print('***Canjear Millas***')
    viajeroDos=viajero-100
    print(viajeroDos)