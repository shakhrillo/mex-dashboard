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
    machineStopped: bool
    barcodeProductionNo: str
    cavity: int
    cycleTime: int
    partStatus: str
    pieceNumber: int
    note: str
    toolCleaning: str
    remainingProductionTime: int
    remainingProductionDays: int
    operatingHours: int
    machineStatus: str