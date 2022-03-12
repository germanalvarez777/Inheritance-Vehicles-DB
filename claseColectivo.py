from claseVehiculo import Vehiculo
from arrayPasajes import ArregloPasajes

class Colectivo(Vehiculo):
    __cantAsientos = None
    __zonas = None
    def __init__ (self,nom,pat,mod, pot, cantidad):
        super().__init__ (nom,pat,mod, pot)
        assert isinstance(cantidad,int),"Tipo de atributo Cant Asientos no es valido"
        self.__cantAsientos = cantidad
        self.__zonas = ArregloPasajes()

    def establecerZonas (self):
        self.__zonas.establecerPasaje(super().getNombreChofer())

    def agregarUnPasajero (self, zona):
        self.__zonas.addContarPasajero (zona, super().getNombreChofer())

    def mostrarVehiculo(self):
        super().mostrarVehiculo()
        print("\n--Datos del Colectivo---")
        print(f"Cantidad de Asientos: {self.__cantAsientos}")
        print("\n===Mostramos la info de sus zonas de pasaje===\n")
        self.__zonas.mostrarPasajes()
        print("\nTotal Viaje Colectivo: {}".format(self.totalViaje()))
        print("\n")

    def totalViaje(self):
        importe = 0
        importe += self.__zonas.total_importe()
        return importe

    def getCantAsientos (self):
        return self.__cantAsientos

    def getZonas (self):
        return self.__zonas