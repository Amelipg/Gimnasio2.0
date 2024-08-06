from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class TipoRespuesta(enum.Enum):
    Abierta = "Abierta"
    SI = "Si"
    NO = "No"

class p_nutricionales(Base):
    __tablename__ = 'tbb_preguntas_nutricionales'

    ID = Column(Integer, primary_key=True, index=True)
    Pregunta = Column(String(20))
    Tipo_Respuesta = Column(Enum(TipoRespuesta))
    Descripcion = Column(String(80))
    Fecha_Creacion = Column(DateTime)
    Fecha_Actualizacion =Column(DateTime)
    Estatus = Column(Boolean, default=False)
    Opciones_Respuesta = Column(String(80))
   