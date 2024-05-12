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

# Enable cors
@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

@app.exception_handler(Exception)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

# Check user token
@app.put("/api/token/", response_model=schemas.UserBase)
def check_token(token: schemas.Token, db: Session = Depends(get_db)):
    return crud.check_token(db=db, token=token)

# @app.get("/api/productionnumber/{bauf}", response_model=schemas.ProductionNumberBase)
# def check_productionnumber(bauf: str):
#     if len(bauf) != 9:
#         return {
#             "Partnumber": '0',
#             "Partname": '0'
#         }
    
#     bauf_aufnr = str(bauf)[:6]
#     bauf_posnr = str(bauf)[6:]
    
#     conn2 = mysql.connector.connect(
#         host=config["DB_HOST"],
#         user=config["DB_USERNAME"],
#         password=config["DB_PASSWORD"],
#         database="alfaplus"
#     )
#     cursor2 = conn2.cursor()
#     cursor2.execute(f"SELECT bauf.bauf_artnr AS Partnumber, bauf.bauf_artbez AS Partname FROM bauf WHERE bauf.bauf_aufnr = '{bauf_aufnr}' AND bauf.bauf_posnr = '{bauf_posnr}' LIMIT 1;")

#     rows = cursor2.fetchall()
#     cursor2.close()
#     conn2.close()

#     if len(rows) == 0:
#         return {
#             "Partnumber": '0',
#             "Partname": '0'
#         }
    
#     return {
#         "Partnumber": rows[0][0],
#         "Partname": rows[0][1]
#     }

@app.post("/api/machines")
def create_machines(machines: schemas.MachineBase, db: Session = Depends(get_db)):
    return crud.create_machines(db=db, machines=machines)

@app.get("/api/status/{user_token}/{machine_id}")
def get_status(user_token: str, machine_id: str, db: Session = Depends(get_db)):
    return crud.get_status(db=db, user_token=user_token, machine_id=machine_id)

@app.get("/api/machines/{user_token}")
def get_machines(user_token: str, db: Session = Depends(get_db)):
    return crud.get_machines(db=db, user_token=user_token)


# @app.get("/api/machines/{machine_id}/status", response_model=schemas.MachineStatusBase)
# def check_machine_status(machine_id: str, db: Session = Depends(get_db)):
#     return crud.get_machine_status(db=db, machineQrCode=machine_id)