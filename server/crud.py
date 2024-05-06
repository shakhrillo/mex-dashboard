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

def get_machine_status(db: Session, machineQrCode: str):
    db_machine = db.query(models.Machine).filter(models.Machine.machineQrCode == machineQrCode).first()
    if db_machine:
        return {
            "machineQrCode": db_machine.machineQrCode,
            "machineStatus": db_machine.machineStatus
        }
    else:
        return {
            "machineQrCode": "Invalid",
            "machineStatus": "Invalid"
        }