from pydantic import BaseModel

class PartInfo(BaseModel):
    title: str
    partName: str
    date: str
    time: float
    type: str

class MachineBase(BaseModel):
    name: str
    status: str

class MainBase(BaseModel):
    machineQrCode: str
    ToolMounted: bool
    MachineMounted: bool
    barcodeProductionNo: str
    partNumber: str
    partName: str
    cavity: int
    cycleTime: int
    partStatus: str
    pieceNumber: int
    note: str
    ToolCleaning: str
    remainingProductionTime: int
    OperatingHours: int

class MainCreate(MainBase):
    pass
