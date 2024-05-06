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
    
def get_productionnumber(db: Session, bauf: int):
    # int 80735001
    # bauf_aufnr = 80735
    # bauf_posnr = 001

    if len(str(bauf)) != 8:
        return {
            "Partnumber": 0,
            "Partname": 0
        }
    
    bauf_aufnr = str(bauf)[:5]
    bauf_posnr = str(bauf)[5:]
    
    bauf_aufnr = int(bauf_aufnr)
    bauf_posnr = int(bauf_posnr)
    
    db_bauf = db.query(models.Bauf).filter(models.Bauf.bauf_artnr == bauf_aufnr).filter(models.Bauf.bauf_artbez == bauf_posnr).first()
    if db_bauf:
        return {
            "Partnumber": db_bauf.bauf_artnr,
            "Partname": db_bauf.bauf_artbez
        }
    else:
        return {
            "Partnumber": 0,
            "Partname": 0
        }