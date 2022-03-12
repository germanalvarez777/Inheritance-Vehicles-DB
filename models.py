import db

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship, Query,query
from datetime import date

#Para que se realize el mapeo entre clase-tabla
#se crean subclases de Base, con los metodos necesarios para definir las columnas y/o claves foraneas.
#además se define una columna x clase como clave primaria, que es manejada automaticamente por la base de datos

#
class Taxis (db.Base):
    __tablename__ = 'Taxis'
    id = Column(Integer, primary_key= True)
    nom = Column (String(80),unique=False,nullable=False)
    pat = Column (String(8),unique=False,nullable=False)
    mod = Column (String(30),unique=False,nullable=False)
    pot = Column (Integer,unique=False,nullable=False)
    lic = Column (Integer,unique=False,nullable=False)
    cantcuadras = Column (Integer,unique=False,nullable=False)         #despues debemos confirmar en la clase menu, cuando se modifique la cant de cuadras (commit)
    totalviaje = Column (Float,unique=False,nullable=False)


#nom,pat,mod, pot, cantidad, totalviaje
class Colectivos (db.Base):
    __tablename__ = 'Colectivos'
    nom = Column (String(80),primary_key=True)
    pat = Column (String(8),unique=False,nullable=False)
    mod = Column (String(30),unique=False,nullable=False)
    pot = Column (Integer,unique=False,nullable=False)
    cant = Column (Integer, unique=False,nullable=False)
    totalviaje = Column (Float,unique=False,nullable=False)

    zonas = relationship('Zonas',backref='Zonas',lazy='dynamic')


class Zonas (db.Base):
    __tablename__ = 'Zonas'
    id = Column (Integer, primary_key=True)
    nro_zona = Column (Integer,unique=False,nullable=False)
    costo = Column (Float,unique=False,nullable=False)
    cant_pasajeros = Column (Integer,unique=False,nullable=False)

    colectivo_nombre = Column (Integer,ForeignKey(Colectivos.nom))
