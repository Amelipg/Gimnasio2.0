from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class PersonasBase(PersonasBase):
    Titulo_Cortesia: str
    Nombre: str
    Primer_Apellido:str
    Segundo_Apellido: str
    Fecha_Nacimiento: datetime
    Fotografia: str
    Genero: str
    Tipo_Sangre: str
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    
class PersonaCreate(PersonasBase):
    pass

class PersonaUpdate(PersonasBase):
    pass
    
class Persona(PersonasBase):
    id:int

    class Config:
        orm_mode =True