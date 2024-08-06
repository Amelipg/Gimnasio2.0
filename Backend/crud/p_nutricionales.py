import models.p_nutricionales
import schemas.p_nutricionales
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por ID
def get_p_nutricional(db:Session, id: int):
    return db.query(models.p_nutricionales.p_nutricional).filter(models.p_nutricionales.p_nutricional.ID == id).first()

# Busqueda por nombre
def get_p_nutricional_by_nombre(db:Session, tipo_respuesta: str):
    return db.query(models.p_nutricionales.p_nutricional).filter(models.p_nutricionales.p_nutricional.Tipo_Respuesta == tipo_respuesta).first()

# Buscar todos las personas
def get_p_nutricionales(db:Session, skip: int=0, limit:int=10):
    return db.query(models.p_nutricionales.p_nutricionales).offset(skip).limit(limit).all()

# Crear una nueva personas
def create_p_nutricionales(db:Session, p_nutricionales: schemas.p_nutricionales.p_nutricionalesCreate):
    db_p_nutricionales = models.p_nutricionales.p_nutricionales(
                                    Pregunta=p_nutricionales.Pregunta,
                                    Tipo_Respuesta=p_nutricionales.Tipo_Respuesta,
                                    Descripcion=p_nutricionales.Descripcion,
                                    Fecha_Creacion=p_nutricionales.Fecha_Creacion,
                                    Fecha_Actualizacion=p_nutricionales.Fecha_Actualizacion,
                                    Estatus=p_nutricionales.Estatus,
                                    Opciones_Respuesta=p_nutricionales.Opciones_Respuesta)
                                    
    db.add(db_p_nutricionales)
    db.commit()
    db.refresh(db_p_nutricionales)
    return db_p_nutricionales

# Actualizar una personas por ID
def update_db_p_nutricionales(db:Session, id:int, db_p_nutricional:schemas.db_p_nutricionales.p_nutricionalesUpdate):
    db_p_nutricionales = db.query(models.p_nutricionales.db_p_nutricionales).filter(models.p_nutricionales.db_p_nutricional.ID == id).first()
    if db_p_nutricionales:
        for var, value in vars(db_p_nutricionales).items():
            setattr(db_p_nutricionales, var, value) if value else None
        db.commit()
        db.refresh(db_p_nutricionales)
    return db_p_nutricionales

# Eliminar una personas por ID
def delete_p_nutricionales(db:Session, id:int):
    db_p_nutricionales = db.query(models.p_nutricionales.p_nutricional).filter(models.p_nutricionales.p_nutricional.ID == id).first()
    if db_p_nutricionales:
        db.delete(db_p_nutricionales)
        db.commit()
    return db_p_nutricionales