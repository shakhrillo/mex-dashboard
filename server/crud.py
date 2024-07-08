from datetime import datetime, time, timedelta
from dotenv import dotenv_values
from sqlalchemy.orm import Session
import mysql.connector

from . import models,schemas
config = dotenv_values(".env")

def is_end_of_month():
    today = datetime.now()
    last_day_of_month = today.replace(day=1) + timedelta(days=32 - today.day)
    return today == last_day_of_month and today.weekday() < 5

def check_shift(time):
    # Define the shifts
    shifts = {
        "F1": ("05:55", "13:50"),
        "S2": ("13:55", "21:50"),
        "N3": ("21:55", "05:50")
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

def create_comment(db: Session, comment: schemas.Comment):
    d = dict({
        "comment": comment.comment,
        "preparation_shift": comment.preparation_shift,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "token": comment.token,
        "shift": check_shift(datetime.now().strftime("%H:%M"))
    })
    model = models.Comment(**d)
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

def start_machine(db: Session, user_token: str):
    db_machine = db.query(models.StartMachine).filter(models.StartMachine.token == user_token).order_by(models.StartMachine.id.desc()).first()
    
    if db_machine and db_machine.start_time and not db_machine.end_time:
        return {
            "status": "Invalid",
            "message": "Machine already started"
        }
    start_time = datetime.now()
    d = dict({
        "token": user_token,
        "start_time": start_time
    })
    model = models.StartMachine(**d)
    db.add(model)
    db.commit()
    db.refresh(model)
    return {
        "status": "ok"
    }

def stop_machine(db: Session, user_token: str):
    end_time = datetime.now()
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
    
def get_machine_status(db: Session, machine_id: str):
    db_machines = db.query(models.MachineData).filter(models.MachineData.machineQrCode == machine_id)
    # order by remainingProductionTime and remainingProductionDays
    # db_machines = db_machines.order_by(models.MachineData.remainingProductionTime.desc(), models.MachineData.remainingProductionDays.desc())
    # get the latest
    db_machines = db_machines.order_by(models.MachineData.createdAt.desc())
    # get all data
    db_machine = db_machines.first()

    if db_machine is None:
        return {
            "status": "Invalid",
            "message": "Not found"
        }

    # Get part number and part name
    conn2 = mysql.connector.connect(
        host=config["DB_HOST"],
        user=config["DB_USERNAME"],
        password=config["DB_PASSWORD"],
        database="alfaplus"
    )
    cursor2 = conn2.cursor()

    bauf_aufnr = str(db_machine.barcodeProductionNo)[:6]
    bauf_posnr = str(db_machine.barcodeProductionNo)[6:]

    cursor2.execute(f"SELECT bauf.bauf_artnr AS Partnumber, bauf.bauf_artbez AS Partname FROM bauf WHERE bauf.bauf_aufnr = '{bauf_aufnr}' AND bauf.bauf_posnr = '{bauf_posnr}' LIMIT 1;")
    productionnumber = cursor2.fetchall()
    if len(productionnumber) == 0:
        productionnumber = [('0', '0')]
    db_machine.partnumber = productionnumber[0][0]
    db_machine.partname = productionnumber[0][1]

    cursor2.close()
    conn2.close()

    return db_machine
    
    
def get_machines(db: Session, user_token: str):
    user_machines = db.query(models.MachineData).filter(models.MachineData.token == user_token).all()

    conn2 = mysql.connector.connect(
        host=config["DB_HOST"],
        user=config["DB_USERNAME"],
        password=config["DB_PASSWORD"],
        database="alfaplus"
    )
    cursor2 = conn2.cursor()
    
    for i in range(len(user_machines)):
        bauf_aufnr = str(user_machines[i].barcodeProductionNo)[:6]
        bauf_posnr = str(user_machines[i].barcodeProductionNo)[6:]
        cursor2.execute(f"SELECT bauf.bauf_artnr AS Partnumber, bauf.bauf_artbez AS Partname FROM bauf WHERE bauf.bauf_aufnr = '{bauf_aufnr}' AND bauf.bauf_posnr = '{bauf_posnr}' LIMIT 1;")
        productionnumber = cursor2.fetchall()
        if len(productionnumber) == 0:
            productionnumber = [('0', '0')]
        user_machines[i].partnumber = productionnumber[0][0]
        user_machines[i].partname = productionnumber[0][1]

    # Return for today only
    today = datetime.now().strftime("%Y-%m-%d")
    user_machines = [machine for machine in user_machines if machine.createdAt.strftime("%Y-%m-%d") == today]

    cursor2.close()
    conn2.close()

    return user_machines

def get_all_machines(db: Session, machine_id: str):
    db_machines = db.query(models.MachineData).filter(models.MachineData.machineQrCode == machine_id)
    # order by date
    db_machines = db_machines.order_by(models.MachineData.createdAt.desc())
    # get all data
    db_machines = db_machines.all()
    return db_machines

def get_status(db: Session, user_token: str, machine_id: str):
    # shift time
    shift = check_shift(datetime.now().strftime("%H:%M"))
    # get user machines
    user_machines = db.query(models.MachineData).filter(models.MachineData.token == user_token)
    # user_machines = db.query(models.MachineData).filter(models.MachineData.token == user_token).group_by(models.MachineData.shift)
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

def get_all_machines_list(db: Session):
    db_machines = db.query(models.Machine)
    machines = [
        "E 41",
        "E 35-2",

        "E 35-1",
        "E 45-1",
        "E 45-2",
        "F450iA-1",
        "E 50-2",
        "E 50-3",
        "F150iA-1",
        "Emac50-1",
        "Emac50-2",
        "Emac50-3",
        "KM 50-1",
        "KM 80-1",
        "KM 150-1",
        "E 55-1",
        "KM 420-1",
        "E 120-1",
        "E 80-1",
        "F250iA-1"
    ]
    db_machines = db_machines.all()
    db_machines = sorted(db_machines, key=lambda x: machines.index(x.machineQrCode))
    
    # order like above


    return db_machines

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
    print(createdAt)
    md = dict({
        "machineQrCode": machines.machineQrCode,
        "token": machines.token,

        "shift": check_shift(datetime.strptime(createdAt, "%Y-%m-%d %H:%M:%S").strftime("%H:%M")),
        "createdAt": datetime.strptime(createdAt, "%Y-%m-%d %H:%M:%S"),
        
        "toolMounted": machines.toolMounted,
        "machineStopped": machines.machineStopped,
        "toolNo": machines.toolNo,
    })

    # if md["toolMounted"] == True:
    #     md["machineStopped"] = True

    # if md["machineStopped"] == False:
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

    # if is_end_of_month() and md["operatingHours"] == 0:
    #     return {
    #         "status": "Invalid",
    #         "message": "Operating hours must be filled out at the end of the month"
    #     }

    model = models.MachineData(**md)
    db.add(model)
    db.commit()
    db.refresh(model)

    # get user machines data
    shift = check_shift(datetime.now().strftime("%H:%M"))
    user_machines = db.query(models.MachineData).filter(models.MachineData.token == machines.token)
    user_machines = user_machines.filter(models.MachineData.createdAt.like(f"{datetime.now().strftime('%Y-%m-%d')}%"))
    user_machines = user_machines.filter(models.MachineData.shift == shift)
    # unique machine names without using group_by
    # user_machines = user_machines.group_by(models.MachineData.machineQrCode)
    
    user_machines = user_machines.all()

    unique_machines = []

    for machine in user_machines:
        if machine.machineQrCode not in unique_machines:
            unique_machines.append(machine.machineQrCode)

    return {
        "status": "ok",
        "total": len(unique_machines)
    }


def update_machines(db: Session, machine_id: str, machines):
    db_machine = db.query(models.MachineData).filter(models.MachineData.id == machine_id).first()

    if db_machine is None:
        return {
            "status": "Invalid",
            "message": "Machine not found"
        }
    
    for key, value in machines.items():
        setattr(db_machine, key, value)

    db.commit()
    db.refresh(db_machine)

    return db_machine