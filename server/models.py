from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Machine(Base):
    __tablename__ = "machines"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    status = Column(String(255), index=True)

class PartInfo(Base):
    __tablename__ = "partinfo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    partName = Column(String(255), index=True)
    date = Column(String(255), index=True)
    time = Column(Float, index=True)
    type = Column(String(255), index=True)

class Main(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    machineQrCode = Column(String(255), index=True)
    ToolMounted = Column(Boolean, index=True)
    MachineMounted = Column(Boolean, index=True)
    barcodeProductionNo = Column(String(255), index=True)
    partNumber = Column(String(255), index=True)
    partName = Column(String(255), index=True)
    cavity = Column(Integer, index=True)
    cycleTime = Column(Integer, index=True)
    partStatus = Column(String(255), index=True)
    pieceNumber = Column(Integer, index=True)
    note = Column(String(255), index=True)
    ToolCleaning = Column(String(255), index=True)
    remainingProductionTime = Column(Integer, index=True)
    OperatingHours = Column(Integer, index=True)
    