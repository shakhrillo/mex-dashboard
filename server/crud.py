from sqlalchemy.orm import Session

from . import models,schemas

def create_machines(db: Session, machines: list[schemas.MachineBase]):
    for machine in machines:
        db_machine = models.Machine(**machine.dict())
        # all_machines = db.query(models.Machine).all()

        # if all_machines:
        #     pass

        # try:
        #     db_machine_exists = db.query(models.Machine).filter(models.Machine.name == db_machine.name).first()
        # except:
        #     db_machine_exists = None
        # if db_machine_exists:
        #     pass
        # else:
        db.add(db_machine)
    db.commit()
    return machines

def get_machines(db: Session):
    machines = db.query(models.Machine).order_by(models.Machine.id).all()
    for machine in machines:
        infos = db.query(models.PartInfo).filter(models.PartInfo.partName == machine.name).all()
        machine.infos = infos
        
    return machines

def create_partinfo(db: Session, partinfo: schemas.PartInfo):
    db_partinfo = models.PartInfo(**partinfo.dict())
    db.add(db_partinfo)
    db.commit()
    db.refresh(db_partinfo)
    return partinfo

def create_main(db: Session, main: schemas.MainBase):
    db_main = models.Main(**main.dict())
    db.add(db_main)
    db.commit()
    db.refresh(db_main)
    print(db_main)
    return main


def get_main(db: Session, main_id: int):
    return db.query(models.Main).filter(models.Main.id == main_id).first()

def get_mains(db: Session):
    return db.query(models.Main).all()
