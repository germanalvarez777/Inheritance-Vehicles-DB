from random import randint
from claseVehiculo import Vehiculo
from claseColectivo import Colectivo
from claseTaxi import Taxi

from models import db
from models import Taxis,Colectivos,Zonas
from sqlalchemy.orm import query, Query

class ManejaVehiculos(object):
    __vehiculos = None
    def __init__ (self):
        self.__vehiculos = []
    
    def agregarVehiculo (self,unVehic):
        if isinstance(unVehic,Vehiculo):
            self.__vehiculos.append (unVehic)
        else:
            print("\nInstancia de vehiculo no es adecuada!\n")

    def cargarVehiculo (self):
        vehiculo = None
        nom_chofer = input("\nIntroduzca el nombre del chofer: ")
        patente = input("\nIngrese la patente del vehiculo: ")
        modelo = input("\nIngrese su modelo: ")
        potencia = int(input("\nIngrese la potencia del vehiculo: "))
        tipo = input("\nIngrese Tipo Vehiculo:\n-->1) Taxi\n-->2) Colectivo\n--> ")
        if tipo == '1':
            licencia = int(input("\nIngrese el numero de licencia: "))
            cant = int(input("\nIngrese la cantidad de cuadras por cada viaje: "))
            vehiculo = Taxi(nom_chofer,patente,modelo,potencia,licencia,cant)

            vehic_db = Taxis (
                nom = nom_chofer,
                pat = patente,
                mod = modelo,
                pot = potencia,
                lic = licencia,
                cantcuadras = cant,       #podemos incrementar este valor? prox opcion a implementar
                totalviaje = vehiculo.totalViaje()
            )
            db.session.add (vehic_db)
            db.session.commit()

        elif tipo == '2':
            cant_asientos = int(input("\nIngrese la cantidad de asientos del colectivo: "))
            vehiculo = Colectivo(nom_chofer, patente,modelo,potencia,cant_asientos)
            vehiculo.establecerZonas()
            cant = int(input("\nIngrese la cantidad de personas ubicadas dentro del mismo: "))
            while cant > cant_asientos:
                cant = int(input("\nIngrese de nuevo,la cantidad de personas ubicadas dentro del mismo: "))
            for i in range (cant):
                azar = randint(1,5)
                vehiculo.agregarUnPasajero(azar)

            vehic_db = Colectivos (
                nom = nom_chofer,
                pat = patente,
                mod = modelo,
                pot = potencia,
                cant = cant_asientos,           
                totalviaje = vehiculo.totalViaje()            
            )

            db.session.add (vehic_db)
            db.session.commit()

        else:
            print("\nTipo de vehiculo ingresado no es correcto!")

        self.agregarVehiculo(vehiculo)


    def mostrarVehiculos (self):
        for vehic in self.__vehiculos:
            print(''.center(45,'='))      
            vehic.mostrarVehiculo()

    def mostrarCantidad (self):
        cant_taxis = 0
        cant_colec = 0
        for vehic in self.__vehiculos:
            if isinstance(vehic,Colectivo):
                cant_colec += 1
            elif isinstance (vehic,Taxi):
                cant_taxis += 1
        
        print(f"Cantidad de Taxis: {cant_taxis} - Cantidad de Colectivos: {cant_colec}\n")

    def totalEmpresa (self):
        total = 0
        for vehic in self.__vehiculos:
            total += vehic.totalViaje()

        print("\nTotal de viaje a rendir por la Empresa: {:.2f}".format(total))

    def buscarColectivo (self, nombre):
        retorna = None
        for vehic in self.__vehiculos:
            if isinstance(vehic,Colectivo):
                if vehic.getNombreChofer().lower() == nombre.lower():
                    zona = int(input("\nIngrese una Zona (1-5): "))
                    while zona <= 1 and zona >= 5:
                        zona = int(input("\nIngrese de nuevo,una Zona (1-5): "))
                    cant = int(input("\nIngrese la cantidad de pasajeros que han ingresado: "))
                    while cant > vehic.getCantAsientos():
                        cant = int(input("\nIngrese de nuevo,la cantidad de pasajeros que han ingresado: "))

                    zonas = vehic.getZonas()
                    for i in range (cant):
                        pasaje = zonas.getUnaZona(zona)

                        zona_db = db.session.query(Zonas).filter_by(nro_zona = zona, colectivo_nombre = vehic.getNombreChofer()).first()
                        #zona_db  = db.session.query(Zonas).filter(Zonas.id == zona).all()
                        if zona_db != None:
                            zona_db.cant_pasajeros += 1
                            db.session.commit()

                        colec_db = db.session.query(Colectivos).filter_by(nom = vehic.getNombreChofer()).first()
                        #colec_db = db.session.query(Colectivos).filter(Colectivos.nom == vehic.getNombreChofer()).all()

                        pasaje.contarPasajero()

                        if colec_db != None:
                            colec_db.totalviaje = vehic.totalViaje()
                            db.session.commit()

                        
                    retorna = True
                    break

        return retorna

    def buscarTaxi (self, nombre):
        i = 0
        exito = None
        while i < len(self.__vehiculos):
            if self.__vehiculos[i].getNombreChofer().lower() == nombre.lower():
                if isinstance (self.__vehiculos[i], Taxi):
                    cant = int(input("\nIngrese la nueva cant de cuadras recorridas: "))
                    self.__vehiculos[i].acumCantidadCuadras(cant)

                    taxi_db = db.session.query(Taxis).filter_by(nom = self.__vehiculos[i].getNombreChofer()).first()
                    if taxi_db != None:
                        taxi_db.cantcuadras += cant
                        taxi_db.totalviaje = self.__vehiculos[i].totalViaje()
                        db.session.commit()

                    exito = True
                    break
                else:
                    print("\nEl conductor %s no maneja un TAXI !"%(nombre.title()))

            i += 1
        
        return exito


