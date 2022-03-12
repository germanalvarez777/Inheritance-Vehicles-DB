from claseVehiculo import Vehiculo
class Taxi (Vehiculo):
    __licencia = None
    costo_Bajada = 300
    increm_cuadra = 75
    __cantCuadras = None
    def __init__ (self,nom,pat,mod, pot,lic,cantcuadras):
        super().__init__(nom,pat,mod, pot)
        assert isinstance (lic, int),"El atributo Licencia no es el adecuado"
        assert isinstance(cantcuadras, int),"El atributo Cantidad de Cuadras no es el adecuado"
        self.__licencia = lic
        self.__cantCuadras = cantcuadras
    
    @classmethod
    def setCostoBajada (cls, valor):
        cls.costo_Bajada = valor
    @classmethod
    def getCostoBajada (cls):
        return cls.costo_Bajada
    
    @classmethod
    def setIncrementoCuadra (cls, valor):
        cls.increm_cuadra = valor
    @classmethod
    def getIncrementoCuadra (cls):
        return cls.increm_cuadra

    def mostrarVehiculo(self):
        super().mostrarVehiculo()
        print("\n---Datos del Taxi---")
        print(f"Numero de Licencia: {self.__licencia} - Costo Bajada: {Taxi.costo_Bajada}\nIncremento por cuadra: {Taxi.increm_cuadra} - Cantidad de Cuadras: {self.__cantCuadras}")
        print("\nTotal Viaje Taxi: %.2f"%(self.totalViaje()))


    def acumCantidadCuadras (self, cant):
        self.__cantCuadras += cant

    def getLicencia (self):
        return self.__licencia
    def getCantCuadras (self):
        return self.__cantCuadras

    def totalViaje(self):
        importe = float(Taxi.getCostoBajada() + (Taxi.getIncrementoCuadra() * self.__cantCuadras))
        importe = round(importe,2)
        return importe
