from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.p_nutricionales, config.db, schemas.p_nutricionales, models.p_nutricionales
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

p_nutricional = APIRouter()
models.p_nutricionales.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los Personas
@p_nutricional.get('/p_nutricional/', response_model=List[schemas.p_nutricionales.p_nutricional],tags=['Preguntas'])
def read_p_nutricionales(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_p_nutricionales = crud.p_nutricionales.get_p_nutricional(db=db,skip=skip, limit=limit)
    return db_p_nutricionales

# Ruta para obtener un Persona por ID
@p_nutricional.post("/p_nutricional/{id}", response_model=schemas.p_nutricionales.p_nutricional, tags=["Preguntas"])
def read_p_nutricionales(id: int, db: Session = Depends(get_db)):
    db_p_nutricionales= crud.p_nutricionales.get_p_nutricional(db=db, id=id)
    if db_p_nutricionales is None:
        raise HTTPException(status_code=404, detail="Pregunta not found")
    return db_p_nutricionales

# Ruta para crear un usurio
@p_nutricional.post('/p_nutricionales/', response_model=schemas.p_nutricionales.p_nutricional,tags=['Preguntas'])
def create_p_nutricionales(p_nutricional: schemas.p_nutricionales.p_nutricionalCreate, db: Session=Depends(get_db)):
    db_p_nutricionales = crud.p_nutricionales.get_p_nutricional_by_nombre(db,tipo_respuesta=p_nutricional.Tipo_Respuesta)
    if db_p_nutricionales:
        raise HTTPException(status_code=400, detail="Pregunta existente intenta nuevamente")
    return crud.p_nutricionales.create_p_nutricionales(db=db, p_nutricional=p_nutricional)

# Ruta para actualizar un Persona
@p_nutricional.put('/p_nutricionales/{id}', response_model=schemas.p_nutricionales.p_nutricional,tags=['Preguntas'])
def update_p_nutricionales(id:int,person: schemas.p_nutricionales.p_nutricionalUpdate, db: Session=Depends(get_db)):
    db_p_nutricionales = crud.p_nutricionales.update_db_p_nutricionales(db=db, id=id, p_nutricional=p_nutricional)
    if db_p_nutricionales is None:
        raise HTTPException(status_code=404, detail="Pregunta no existe, no se pudo actualizar ")
    return db_p_nutricionales

# Ruta para eliminar un Persona
@p_nutricional.delete('/p_nutricionales/{id}', response_model=schemas.p_nutricionales.p_nutricional,tags=['Preguntas'])
def delete_p_nutricionales(id:int, db: Session=Depends(get_db)):
    db_p_nutricionales = crud.p_nutricionales.delete_p_nutricionales(db=db, id=id)
    if db_p_nutricionales is None:
        raise HTTPException(status_code=404, detail="Pregunta no existe, no se pudo eliminar ")
    return db_p_nutricionales