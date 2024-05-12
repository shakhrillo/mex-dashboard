from datetime import datetime, time, timedelta
from sqlalchemy.orm import Session

from . import models,schemas

def is_end_of_month():
    today = datetime.now()
    last_day_of_month = today.replace(day=1) + timedelta(days=32 - today.day)
    return today == last_day_of_month and today.weekday() < 5

def check_shift(time):
    # Define the shifts
    shifts = {
        "F1": ("06:00", "14:30"),
        "S2": ("14:00", "22:30"),
        "N3": ("22:00", "06:30")
    }

    # Convert time strings to datetime objects for easier comparison
    time_obj = datetime.strptime(time, "%H:%M")

    # Check which shift the time falls into
    for shift, (start, end) in shifts.items():
        start_obj = datetime.strptime(start, "%H:%M")
        end_obj = datetime.strptime(end, "%H:%M")

        if start_obj <= time_obj < end_obj or (start_obj > end_obj and (time_obj >= start_obj or time_obj < end_obj)):
            return shift

    return None

def start_machine(db: Session, user_token: str):
    today = datetime.now().strftime("%Y-%m-%d")
    db_machine = db.query(models.StartMachine).filter(models.StartMachine.token == user_token).order_by(models.StartMachine.id.desc())
    db_machine = db_machine.filter(models.StartMachine.start_time.like(f"{today}%")).first()
    if db_machine:
        return {
            "status": "Invalid",
            "message": "Machine already started"
        }
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    d = dict({
        "token": user_token,
        "start_time": start_time,
        "shift": check_shift(datetime.now().strftime("%H:%M"))
    })
    model = models.StartMachine(**d)
    db.add(model)
    db.commit()
    db.refresh(model)
    return {
        "status": "ok"
    }

def stop_machine(db: Session, user_token: str):
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    db_machine = db.query(models.StartMachine).filter(models.StartMachine.token == user_token).order_by(models.StartMachine.id.desc()).first()
    if db_machine:
        db_machine.end_time = end_time
        db.commit()
        db.refresh(db_machine)
        return {
            "status": "ok"
        }
    else:
        return {
            "status": "Invalid",
            "message": "Start time not found"
        }


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
    
def get_machines(db: Session, user_token: str):
    user_machines = db.query(models.MachineData).filter(models.MachineData.token == user_token).all()
    return user_machines

def get_status(db: Session, user_token: str, machine_id: str):
    # shift time
    shift = check_shift(datetime.now().strftime("%H:%M"))
    # get user machines
    user_machines = db.query(models.MachineData).filter(models.MachineData.token == user_token).group_by(models.MachineData.shift)
    # get today's data
    user_machines = user_machines.filter(models.MachineData.createdAt.like(f"{datetime.now().strftime('%Y-%m-%d')}%"))
    # get shift data
    user_machines = user_machines.filter(models.MachineData.shift == shift)
    # get machine data
    user_machines = user_machines.filter(models.MachineData.machineQrCode == machine_id)
    user_machines = user_machines.all()
    
    if len(user_machines) == 0:
        return {
            "status": "Invalid",
            "message": "Not found"
        }
    
    return {
        "status": "ok",
        "message": user_machines
    }


def create_machines(db: Session, machines):
    db_machine = db.query(models.Machine).filter(models.Machine.machineQrCode == machines.machineQrCode).first()

    if db_machine is None:
        d = dict({
            "machineQrCode": machines.machineQrCode        
        })
        db_machine = models.Machine(**d)
        db.add(db_machine)
        db.commit()
        db.refresh(db_machine)

    # check user token
    db_token = db.query(models.User).filter(models.User.token == machines.token).first()
    if db_token is None:
        return {
            "status": "Invalid",
            "message": "Token not found"
        }

    # date and time format with python
    createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    md = dict({
        "machineQrCode": machines.machineQrCode,
        "token": machines.token,

        "shift": check_shift(datetime.now().strftime("%H:%M")),
        "createdAt": createdAt,
        
        "toolMounted": machines.toolMounted,
        "machineStopped": machines.machineStopped
    })

    if md["toolMounted"] == True:
        md["machineStopped"] = True

    if md["machineStopped"] == False:
        md["barcodeProductionNo"] = machines.barcodeProductionNo
        md["cavity"] = machines.cavity
        md["cycleTime"] = machines.cycleTime
        md["partStatus"] = machines.partStatus
        md["pieceNumber"] = machines.pieceNumber
        md["note"] = machines.note
        md["toolCleaning"] = machines.toolCleaning
        md["remainingProductionTime"] = machines.remainingProductionTime
        md["remainingProductionDays"] = machines.remainingProductionDays
        md["operatingHours"] = machines.operatingHours

    if is_end_of_month() and md["operatingHours"] == 0:
        return {
            "status": "Invalid",
            "message": "Operating hours must be filled out at the end of the month"
        }

    model = models.MachineData(**md)
    db.add(model)
    db.commit()
    db.refresh(model)

    # get user machines data
    shift = check_shift(datetime.now().strftime("%H:%M"))
    user_machines = db.query(models.MachineData).filter(models.MachineData.token == machines.token)
    user_machines = user_machines.filter(models.MachineData.createdAt.like(f"{datetime.now().strftime('%Y-%m-%d')}%"))
    user_machines = user_machines.filter(models.MachineData.shift == shift)
    user_machines = user_machines.group_by(models.MachineData.machineQrCode)
    user_machines = user_machines.all()

    return {
        "status": "ok",
        "total": len(user_machines),
    }

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


    if len(bauf) != 9:
        return {
            "Partnumber": '0',
            "Partname": '0'
        }
    
    bauf_aufnr = str(bauf)[:6]
    bauf_posnr = str(bauf)[6:]

    # show last 3 
    raw = db2.query(models.Bauf).first()
    print('-------------------')
    print(raw)
    print(raw['bauf_artnr'])
    print(raw['bauf_artbez'])
    print('-------------------')
    
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