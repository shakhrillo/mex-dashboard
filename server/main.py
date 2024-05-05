from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from . import crud,models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()

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

@app.post("/api/machines/", response_model=list[schemas.MachineBase])
def create_machine(machines: list[schemas.MachineBase], db: Session = Depends(get_db)):
    return crud.create_machines(db=db, machines=machines)

@app.get("/machines/")
def read_machines(db: Session = Depends(get_db)):
    machines = crud.get_machines(db)
    return machines

@app.post("/api/partinfo/", response_model=schemas.PartInfo)
def create_partinfo(partinfo: schemas.PartInfo, db: Session = Depends(get_db)):
    return crud.create_partinfo(db=db, partinfo=partinfo)

@app.post("/api/main/", response_model=schemas.MainBase)
def post_main(main:schemas.MainBase, db:Session=Depends(get_db)):
    return crud.create_main(db=db,main=main)

@app.get("/mains/")
def get_mains(db:Session=Depends(get_db)):
    mains = crud.get_mains(db)
    return mains

@app.get("/main/{main_id}/",response_model=schemas.MainBase)
def get_main(main_id:int, db:Session=Depends(get_db)):
    db_main = crud.get_main(db,main_id=main_id )
    if db_main is None:
        raise HTTPException(status_code=404, detail="Main not found")
    return db_main