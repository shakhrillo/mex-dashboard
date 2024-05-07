from sqlalchemy.orm import Session

from . import models,schemas

def check_token(db: Session, token: schemas.Token):
    db_token = db.query(models.User).filter(models.User.token == token.token).first()
    if db_token:
        return {
            "name": db_token.name,
            "surname": db_token.surname,
            "token": db_token.token
        }
    else:
        return {
            "name": "Invalid",
            "surname": "Invalid",
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
            "machineStatus": db_machine.machineStatus,
            "productNo": db_machine.barcodeProductionNo
        }
    else:
        return {
            "machineQrCode": "Invalid",
            "machineStatus": "Invalid",
            "productNo": 0
        }
    
def get_productionnumber(db2: Session, bauf: str):
    # int 80735001
    # int 811471001
    # bauf_aufnr = 811471
    # bauf_posnr = 001


    print(len(bauf))
    print(bauf)
    print(str(bauf)[:6])
    print(str(bauf)[6:])


    if len(bauf) != 9:
        return {
            "Partnumber": '0',
            "Partname": '0'
        }
    
    bauf_aufnr = str(bauf)[:6]
    bauf_posnr = str(bauf)[6:]
    
    db_bauf = db2.query(models.Bauf).filter(models.Bauf.bauf_artnr == bauf_aufnr).filter(models.Bauf.bauf_artbez == bauf_posnr).first()
    if db_bauf:
        return {
            "Partnumber": db_bauf.bauf_artnr,
            "Partname": db_bauf.bauf_artbez
        }
    else:
        return {
            "Partnumber": '0',
            "Partname": '0'
        }