from sqlalchemy.orm import Session

from . import models,schemas

def check_token(db: Session, token: schemas.Token):
    db_token = db.query(models.User).filter(models.User.token == token.token).first()
    if db_token:
        return {
            "username": db_token.username,
            "token": db_token.token
        }
    else:
        return {
            "username": "Invalid",
            "token": "Invalid"
        }

def create_machines(db: Session, machines: schemas.MachineBase):
    db_machine = models.Machine(**machines.dict())
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return machines