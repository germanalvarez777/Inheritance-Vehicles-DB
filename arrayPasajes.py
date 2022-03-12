import numpy as np
from clasePasaje import Pasaje

from models import db
from models import Zonas
from sqlalchemy.orm import query, Query, session

class ArregloPasajes (object):
    __cantidad = None
    __dimension = None
    def __init__ (self):
        self.__dimension = 5
        self.__cantidad = 0
        self.__pasajes = np.empty (5, dtype=Pasaje)

    def agregarPasaje (self,costoPasaje, nombre_col):
        #print("Ejecuta agregar pasaje")
        if self.__cantidad < 5:
            unPasaje = Pasaje (costoPasaje)
            self.__pasajes[self.__cantidad] = unPasaje

            pasaje_db = Zonas (
                nro_zona = self.__cantidad + 1,
                costo = costoPasaje,
                cant_pasajeros = 0,
                colectivo_nombre = nombre_col
                )

            db.session.add (pasaje_db)
            db.session.commit()

            #print(f"Self.cantidad = {self.__cantidad} - self.pasaj[i] = {self.__pasajes[self.__cantidad]}")
            self.__cantidad += 1
        else:
            raise Exception ('\nLa cantidad de zonas es superior a Cinco!')

    def addContarPasajero (self, nroZona, nom):
        #una forma es hacerlo con while y bandera
        #otra forma: con for y break

        if nroZona >= 1 and nroZona <= 5:
            nroZona -= 1
            for i in range(self.__cantidad):
                if i == nroZona:
                    self.__pasajes[i].contarPasajero()
                    
                    zona_db = db.session.query(Zonas).filter_by(nro_zona = nroZona+1, colectivo_nombre = nom).first()
                    
                    if zona_db != None:
                        zona_db.cant_pasajeros += 1
                        db.session.commit()

                    break
        else:
            raise Exception ('\nNumero de Zona no es valido!')

    def total_importe (self):
        imp = 0.0
        for i in range(self.__cantidad):
            imp += float(self.__pasajes[i].getCosto() * self.__pasajes[i].getCantidad())

        imp = round (imp,2)
        return imp


    def mostrarPasajes (self):
        for i in range (self.__cantidad):
            print("*".center(25,'*'))
            self.__pasajes[i].mostrarPasaje()

    def establecerPasaje (self, nombre):
        base = 30
        for k in range(5):
            if k == 2:
                base = 45
                self.agregarPasaje(base, nombre)
                base += 5
            elif k == 4:
                self.agregarPasaje(65, nombre)
            else:
                self.agregarPasaje(base, nombre)
                base += 5


    def getUnaZona (self, zona):
        assert zona <= self.__cantidad, "El valor de Zona a buscar NO es VALIDO"
        return self.__pasajes[zona-1]