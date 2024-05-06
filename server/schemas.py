from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    token: str

class Token(BaseModel):
    token: str

class MachineBase(BaseModel):
    token: str
    machineQrCode: str
    toolMounted: bool
    machineMounted: bool
    barcodeProductionNo: str
    cavity: int
    cycleTime: str
    partStatus: str
    pieceNumber: int
    note: str
    toolCleaning: str
    remainingProductionTime: int
    operatingHours: int
    machineStatus: str

class MachineStatusBase(BaseModel):
    machineQrCode: str
    machineStatus: str
    productNo: int

class ProductionNumberBase(BaseModel):
    Partnumber: int
    Partname: int