class PlanAhorro:
    __codigo = ''
    __modelo =''
    __version =''
    __valor = 0.0
    __cantidadcuotasDelPlan = 0
    __cantidadDeCuotasPagas = 0

    def __init__(self,codigo='',modelo='',version='',valor=0.0):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
    def __str__(self):
        return'Codigo de plan: {} modelo:{} version:{}'.format(self.__codigo,self.__modelo,self.__version)
    def setValor(self,valor):
        self.__valor = valor
    @classmethod
    def setCantidadCuotasPlan(cls,cuota):
        cls.__cantidadcuotasDelPlan=cuota
    @classmethod
    def setCantidadCuotasParaLicitar(cls,cuota):
        cls.__cantidadDeCuotasPagas=cuota
    def valorDeCuota(self):
        valorDeCuota = (self.__valor/self.__cantidadcuotasDelPlan)+self.__valor*0.10
        return valorDeCuota
    def getValor(self):
        return self.__valor
    def montoParaLicitar(self):
        return self.__cantidadDeCuotasPagas*self.valorDeCuota()
    def getCodigo(self):
        return self.__codigo