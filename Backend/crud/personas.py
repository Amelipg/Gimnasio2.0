from sqlalchemy.orm import Session
import models.personas
import schemas.personas
import models, schemas

def get_persona(db:Session, id: int):
    return db.query(models.personas.Persona).filter(models.personas.Persona.id== id).first()

def get_persona_by_usuario(db:Session, usuario: str):
    return db.query(models.personas.Persona).filter(models.personas.Persona.usuario== usuario).first()

def get_personas(db:Session, skip: int = 0, limit: int = 10):
    return db.query(models.personas.Persona).offset(skip).limit(limit).all()

def create_persona(db: Session, persona:schemas.personas.PersonaCreate):
    db_persona=models.personas.Persona(usuario=persona.usuario, password=persona.password, created_at=persona.created_at, estatus=persona.estatus, Id_persona=persona.Id_persona)
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona

def update_persona(db:Session, id: int, persona:schemas.personas.PersonaUpdate):
    db_persona= db.query(models.personas.Persona).filter(models.personas.Persona.id== id).first()
    if db_persona:
        for var, value in vars(persona).items():
            setattr(db_persona, var, value) if value else None
        db.commit()
        db.refresh(db_persona)
    return db_persona

def delete_persona(db:Session, id: int):
    db_persona= db.query(models.personas.Persona).filter(models.personas.Persona.id== id).first()
    if db_persona:
        db.delete(db_persona)
        db.commit()
    return db_persona
