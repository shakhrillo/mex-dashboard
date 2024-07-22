from dotenv import dotenv_values
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

config = dotenv_values(".env")
import mysql.connector
from . import crud,models, schemas
from .database import SessionLocal, SessionLocal_2, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()

def get_db_2():
    db2 = SessionLocal_2()
    try : 
        yield db2
    finally:
        db2.close()

# Enable cors for http://192.168.100.23:3230/
# enbale for localhost
@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response
    
# @app.middleware("http")
# async def add_cors_header(request, call_next):
#     response = await call_next(request)
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Methods"] = "*"
#     response.headers["Access-Control-Allow-Headers"] = "*"
#     return response

@app.exception_handler(Exception)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

@app.put("/api/token/", response_model=schemas.UserBase)
def check_token(token: schemas.Token, db: Session = Depends(get_db)):
    return crud.check_token(db=db, token=token)

@app.post("/api/comments/")
def create_comment(comment: schemas.Comment, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment, user_token=comment.user_token)

@app.get("/api/machines/{user_token}/start")
def start_machine(user_token: str, db: Session = Depends(get_db)):
    return crud.start_machine(db=db, user_token=user_token)

@app.get("/api/machines/{user_token}/stop")
def stop_machine(user_token: str, db: Session = Depends(get_db)):
    return crud.stop_machine(db=db, user_token=user_token)

@app.post("/api/machines")
def create_machines(machines: schemas.MachineBase, db: Session = Depends(get_db)):
    return crud.create_machines(db=db, machines=machines)

@app.put("/api/machines/{machine_id}")
def update_machines(machine_id: str, machines: dict, db: Session = Depends(get_db)):
    return crud.update_machines(db=db, machine_id=machine_id, machines=machines)

@app.get("/api/machines")
def get_machines(db: Session = Depends(get_db)):
    return crud.get_all_machines_list(db=db)

@app.get("/api/machine/status/{machine_id}")
def get_machine_status(machine_id: str, db: Session = Depends(get_db)):
    return crud.get_machine_status(db=db, machine_id=machine_id)

@app.get("/api/machines/{user_token}")
def get_machines(user_token: str, db: Session = Depends(get_db)):
    return crud.get_machines(db=db, user_token=user_token)

@app.get("/api/status/{user_token}/{machine_id}")
def get_status(user_token: str, machine_id: str, db: Session = Depends(get_db)):
    return crud.get_status(db=db, user_token=user_token, machine_id=machine_id)

@app.get("/api/all_machines/{machine_id}")
def get_all_machines(machine_id: str, db: Session = Depends(get_db)):
    return crud.get_all_machines(db=db, machine_id=machine_id)

# http://35.184.23.4/api/current
@app.get("/api/current/{machine_id}")
def get_current(machine_id: str, db: Session = Depends(get_db)):
    last_data = db.query(models.Machine).filter(models.Machine.machineQrCode == machine_id)
    # order by date
    last_data = last_data.order_by(models.Machine.createdAt.desc()).first()
    last_shift = last_data.shift
    last_tool_cleaning = last_data.toolCleaning

    if last_shift == "F1" and last_tool_cleaning == False:
        return {
            "text": "Werkzeugreinigung in Schicht F1 erledigt?",
            "status": "warning",
        }
    
    if last_shift == "S2" and last_tool_cleaning == False:
        return {
            "text": "Achtung – Werkzeugreinigung notwendig!“ „Ist erledigt?",
            "status": "warning",
        }
    
    return {
        "text": "Werkzeugreinigung Schicht F1 erledigt",
        "status": "success",
    }

@app.get("/api/productionnumber/{bauf}")
def check_productionnumber(bauf: str):
    if len(bauf) != 9:
        return {
            "Partnumber": '0',
            "Partname": '0'
        }
    # CREATE TABLE bauf (
    #     bauf_aufnr VARCHAR(6),
    #     bauf_posnr VARCHAR(3),
    #     bauf_artnr VARCHAR(3),
    #     bauf_artbez VARCHAR(50)
    # );
    # INSERT INTO bauf (bauf_aufnr, bauf_posnr, bauf_artnr, bauf_artbez) VALUES
    # ('811202', '001', '001', 'Part 1 Name'),
    # ('765432', '001', '002', 'Part 2 Name'),
    # ('123456', '001', '003', 'Part 3 Name'),
    # ('123456', '002', '004', 'Part 4 Name');

    
    bauf_aufnr = str(bauf)[:6]
    bauf_posnr = str(bauf)[6:]
    
    conn2 = mysql.connector.connect(
        host=config["DB_HOST"],
        user=config["DB_USERNAME"],
        password=config["DB_PASSWORD"],
        database="alfaplus"
    )
    cursor2 = conn2.cursor()
    cursor2.execute(f"SELECT bauf.bauf_artnr AS Partnumber, bauf.bauf_artbez AS Partname FROM bauf WHERE bauf.bauf_aufnr = '{bauf_aufnr}' AND bauf.bauf_posnr = '{bauf_posnr}' LIMIT 1;")

    rows = cursor2.fetchall()
    cursor2.close()
    conn2.close()

    if len(rows) == 0:
        return {
            "Partnumber": '0',
            "Partname": '0'
        }
    
    return {
        "Partnumber": rows[0][0],
        "Partname": rows[0][1]
    }