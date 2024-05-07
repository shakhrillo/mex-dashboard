from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

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

@app.get("/api/productionnumber/{bauf}", response_model=schemas.ProductionNumberBase)
def check_productionnumber(bauf: str, db2: Session = Depends(get_db_2)):
    return crud.get_productionnumber(db2=db2, bauf=bauf)

@app.post("/api/machines", response_model=schemas.MachineBase)
def create_machines(machines: schemas.MachineBase, db: Session = Depends(get_db)):
    return crud.create_machines(db=db, machines=machines)

@app.get("/api/machines/{machine_id}/status", response_model=schemas.MachineStatusBase)
def check_machine_status(machine_id: str, db: Session = Depends(get_db)):
    return crud.get_machine_status(db=db, machineQrCode=machine_id)