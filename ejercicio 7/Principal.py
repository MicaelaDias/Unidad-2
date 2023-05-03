from ViajeroFrecuente import ViajeroFrecuente

if __name__=='__main__':
    viajero=ViajeroFrecuente(230,'42335678','Carlos','Cortez',400)
    print('Comparar millas')
    if viajero==100:
        print('El viajero tiene 100 millas acumuladas')
    else:
        print('El viaero no tiene 100 millas acumuladas')
    if 100==viajero:
        print('El viajero tiene 100 millas acumuladas')
    else:
        print('El viajero no tiene 100 millas acumuladas.')


    print('***Acumular millas***')
    viajeroUno=100+viajero
    print(viajeroUno)
    print('***Canjear Millas***')
    viajeroDos=100-viajero
    print(viajeroDos)