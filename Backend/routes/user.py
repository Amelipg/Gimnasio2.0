from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user = APIRouter()
users = [

]
class models_user(BaseModel):
    id:str
    usuario:str
    contrasena: str
    created_at:datetime = datetime.now()
    estatus:bool=False

@user.get("/")

def Bienvenidos():
    return "Hola 9°B desde el método GET"

@user.get("/users", tags=["Usuarios"])

def get_Users():
    return users

@user.get("/users/{user_id}", tags=["Usuarios"])

def get_User(user_id: str):
    for user in users:
        if user.id == user_id:
            return user

@user.post('/users', tags=["Usuarios"])

def insert_User(insert_user:models_user):
    users.append(insert_user)
    return {"message": f"Se ha insertado un nuevo usuario con el ID: {insert_user.id}"}

@user.put('/users/{user_id}', tags=["Usuarios"])

def update_User(update_user:models_user, user_id: str):
    print(update_user)
    for index, user in enumerate(users):
        if user.id == user_id:
            update_user.created_at = user.created_at
        
            users[index] = update_user
            
            return {"message": f"Se ha modificado correctamente al usuario con el ID: {user_id}"}

@user.delete('/users/{user_id}', tags=["Usuarios"])

def delete_User(user_id: str):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": f"Se ha eliminado correctamente al usuario con el ID: {user_id}"}
        
@user.post("/users/{user_id}", tags=["Usuarios"])

def post_User(user_id: str):
    for user in users:
        if user.id == user_id:
            return user