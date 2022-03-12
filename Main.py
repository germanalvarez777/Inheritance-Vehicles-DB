import os
from claseMenu import Menu

import db
from models import Taxis,Colectivos,Zonas

if __name__ == '__main__':

    db.Base.metadata.drop_all(db.engine)        #eliminar todos los registros de la base de datos
    db.Base.metadata.create_all(db.engine)      #crea las tablas de todos los modelos que se encuentren  importados con anterioridad

    menu = Menu()
    salir = True
    while salir:
        print("""
        =============================================================
        1 - Agregar vehiculos a la colección.
        2 - Mostrar la cantidad de colectivos y taxis almacenados.
        3 - Mostrar información de todos los vehiculos.
        4 - Incrementar pasajeros de algún colectivo.
        5 - Incrementar cantidad de cuadras recorridas de algún taxi.
        6 - Salir.
        =============================================================
        """)
        op = input("\nIngrese una opcion--> ")
        os.system('clear')
        if op != '1' and op != '2' and op != '3' and op != '4' and op != '5' and op != '6':
            salir = False
            print("\nOpcion no valida, fin del programa!")
        else:
            if op == '6':
                menu.salir()
                salir = False
            else:
                menu.opcion (op)
