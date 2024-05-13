from pydantic import BaseModel

class Comment(BaseModel):
    comment: str
    preparation_shift: bool
    token: str

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
    barcodeProductionNo: int
    cavity: int
    cycleTime: str
    partStatus: bool
    pieceNumber: int
    note: str
    toolCleaning: bool
    remainingProductionTime: int
    remainingProductionDays: int
    operatingHours: str