from abc import ABC
import abc

class Vehiculo (ABC):
    __nombreChofer= None
    __patente = None
    __modelo = None
    __potencia = None
    def __init__ (self, nom,pat,mod, pot):
        assert isinstance(nom,str),"Tipo de Atributo Nombre no valido"
        assert isinstance(pat,str),"Tipo de Atributo Patente no valido"       
        assert isinstance(mod,str),"Tipo de Atributo Modelo no valido"
        assert isinstance(pot,int),"Tipo de Atributo Potencia no valido"

        self.__nombreChofer = nom
        self.__patente = pat
        self.__modelo = mod
        self.__potencia = pot
    
    def mostrarVehiculo (self):
        print("\n---Datos del Vehiculo---")
        print(f"Nombre del Chofer: {self.__nombreChofer.title()} - Patente: {self.__patente.upper()}\nModelo: {self.__modelo.capitalize()} - Potencia: {self.__potencia}")

    def getNombreChofer (self):
        return self.__nombreChofer
    def getPatente (self):
        return self.__patente
    def getModelo (self):
        return self.__modelo
    def getPotencia (self):
        return self.__potencia    

    @abc.abstractmethod
    def totalViaje (self):
        pass
