from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

persona = APIRouter()
personas = [

]
class models_persona(BaseModel):
    id:str
    usuario:str
    contrasena: str
    created_at:datetime = datetime.now()
    estatus:bool=False

@persona.get("/")

def Bienvenidos():
    return "Hola 9°B desde el método GET"

@persona.get("/personas", tags=["Personas"])

def get_Personas():
    return personas

@persona.get("/personas/{persona_id}" , tags=["Personas"])

def get_Personas(persona_id: str):
    for persona in personas:
        if persona.id == persona_id:
            return persona

@persona.post('/personas', tags=["Personas"])

def insert_Personas(insert_persona:models_persona):
    personas.append(insert_persona)
    return {"message": f"Se ha insertado una nueva persona con el ID: {insert_persona.id}"}

@persona.put('/personas/{persona_id}', tags=["Personas"])

def update_Persona(update_persona:models_persona, persona_id: str):
    print(update_persona)
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            update_persona.created_at = persona.created_at
        
            personas[index] = update_persona
            
            return {"message": f"Se ha modificado correctamente a la persona con el ID: {persona_id}"}

@persona.delete('/personas/{persona_id}', tags=["Personas"])

def delete_Persona(persona_id: str):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            personas.pop(index)
            return {"message": f"Se ha eliminado correctamente a la persona con el ID: {persona_id}"}
        
@persona.post("/persona/{user_id}", tags=["Personas"])

def post_Persona(persona_id: str):
    for persona in personas:
        if persona.id == persona_id:
            return persona