from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Personas(Base):
    __tablename__= 'personas'
    
    id= Column(Integer, primary_key=True, index=True)
    Ttitulo_Cortesia=Column(String(255))
    Nombre=Column(String(255))
    Primer_Apellido =Column(String(255))
    Segundo_Apellido=Column(String(255))
    Fecha_Nacimiento=Column(DateTime)
    Fotografia=Column(LONGTEXT)
    Genero=Column(String(255))
    Tipo_Sangre=Column(String(255))
    Estatus=Column(Boolean, default=False)
    Fecha_Registro=Column(DateTime)
    Fecha_Actualizacion=Column(DateTime)