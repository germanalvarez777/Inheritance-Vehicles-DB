import os
from ManejaVehiculos import ManejaVehiculos

class Menu (object):
    __switcher = None
    __manejVehiculos = None
    def __init__ (self):
        self.__switcher = {'1': self.opcion1,'2':self.opcion2,'3': self.opcion3,'4': self.opcion4, '5': self.opcion5, '6': self.salir}
        self.__manejVehiculos = ManejaVehiculos()
    
    def salir (self):
        print("\nSalida del Programa! Chao :O")

    def opcion (self, op):
        func = self.__switcher.get(op, lambda:print("\nOpcion no valida"))
        func()
    
    def opcion1 (self):
        input("\nSe ejecuta la OPCION 1-> ")
        self.__manejVehiculos.cargarVehiculo()
        os.system('clear')

    def opcion2 (self):
        input("\nSe ejecuta la OPCION 2-> ")
        self.__manejVehiculos.mostrarCantidad()   
        input("\nHa FINALIZADO la Opcion 2, presione una tecla para continuar: ") 
        os.system('clear')

    def opcion3 (self):
        input("\nSe ejecuta la OPCION 3-> ")
        input("\nMostramos info de TODOS los VEHICULOS cargados: ")
        self.__manejVehiculos.mostrarVehiculos()
        self.__manejVehiculos.totalEmpresa()
        input("\nHa FINALIZADO la Opcion 3, presione una tecla para continuar: ")

        os.system('clear')

    def opcion4 (self):
        input("\nSe ejecuta la OPCION 4-> ")
        nombre = input("\nIngrese el nombre del COLECTIVERO a buscar->\n")
        buscar = self.__manejVehiculos.buscarColectivo(nombre)
        if buscar == None:
            print(f"No se encontro el colectivero con nombre {nombre.title()}")
        else:
            print("Se incremento la cantidad de pasajeros del colectivo de {}".format(nombre.title()))

        input("\nHa FINALIZADO la Opcion 4, presione una tecla para continuar: ")
        os.system('clear')


    #PODEMOS añadir como ultima opcion, incrementar la cantidad de cuadras de un taxi, como un colec incrementa sus pasajeros
    def opcion5 (self):
        input("\nSe ejecuta la OPCION 5-> ")
        nombre = input("\nIngrese el nombre del TAXISTA a buscar->\n")
        buscar = self.__manejVehiculos.buscarTaxi (nombre)
        if buscar != None:
            print(f"\nSe incremento la cantidad de cuadras recorridas del taxi de {nombre.title()}")
        else:
            print("\nNo se encontró el taxista con nombre {}".format(nombre.title()))

        input("\nHa FINALIZADO la Opcion 5, presione una tecla para continuar: ")
        os.system('clear')
