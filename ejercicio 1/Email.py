
class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contrasena = ''

    def __init__(self,idCuenta='',dominio='',tipoDominio='',contrasena=''):
        self.__idCuenta=idCuenta
        self.__dominio=dominio
        self.__tipoDominio=tipoDominio
        self.__contrasena=contrasena
    def getDominio(self):
        return self.__dominio
    def retornaEmail(self):
        return '{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipoDominio)
    def crearCuenta(self,correo):
        if type(correo)==Email:
            print('Se creo la cuenta: {}'.format(correo.retornaEmail()))
    def setContrasena(self,contrasena):
        self.__contrasena=contrasena
    def verificarContrasena(self,conActual):
        bandera=False
        if conActual==self.__contrasena:
            bandera=True
        return bandera   
    def crearEmail(self,correo,contrasena):
        
        separador=correo.split('@')
        idCuenta=separador[0]
        separadorDos=separador[1].split('.')
        dominio=separadorDos[0]
        tipoDeDominio=separadorDos[1]
        emailUno=Email(idCuenta,dominio,tipoDeDominio,contrasena)
        return emailUno