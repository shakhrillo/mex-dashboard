from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    surname: str
    token: str

class Token(BaseModel):
    token: str

class MachineBase(BaseModel):
    shift: str
    token: str
    createdAt: str
    machineQrCode: str
    toolMounted: bool
    machineMounted: bool
    barcodeProductionNo: str
    cavity: int
    cycleTime: int
    partStatus: str
    pieceNumber: int
    note: str
    toolCleaning: str
    remainingProductionDays: int
    remainingProductionTime: int
    operatingHours: int
    machineStatus: str

class MachineStatusBase(BaseModel):
    machineQrCode: str
    machineStatus: str
    productNo: int

class ProductionNumberBase(BaseModel):
    Partnumber: str
    Partname: str