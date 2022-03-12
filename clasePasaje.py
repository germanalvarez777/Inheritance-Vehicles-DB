
class Pasaje(object):
    __costo = None
    __cantPasajeros = None
    def __init__ (self,costo):
        #assert isinstance(costo,float),"Tipo de Atributo Costo no es valido"
        costo = round(costo,2)
        self.__costo = costo
        self.__cantPasajeros = 0
    
    def contarPasajero (self):
        self.__cantPasajeros += 1

    def getCosto (self):
        return self.__costo
    def getCantidad (self):
        return self.__cantPasajeros

    def mostrarPasaje (self):
        #print(f"Costo de Zona: {self.__costo} - Cantidad de Pasajeros: {self.__cantPasajeros}")
        print("Costo de Zona: {} - Cantidad de Pasajeros: {}".format(self.__costo,self.__cantPasajeros))

