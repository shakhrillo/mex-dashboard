from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    surname = Column(String(255), index=True)
    token = Column(String(255), index=True)
class Machine(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    createdAt = Column(String(255), index=True)
    shift = Column(String(255), index=True)
    token = Column(String(255), index=True)
    machineQrCode = Column(String(255), index=True)
    toolMounted = Column(Boolean, index=True)
    machineMounted = Column(Boolean, index=True)
    barcodeProductionNo = Column(String(255), index=True)
    cavity = Column(Integer, index=True)
    cycleTime = Column(Integer, index=True)
    partStatus = Column(String(255), index=True)
    pieceNumber = Column(Integer, index=True)
    note = Column(String(255), index=True)
    toolCleaning = Column(String(255), index=True)
    remainingProductionTime = Column(Integer, index=True)
    remainingProductionDays = Column(Integer, index=True)
    operatingHours = Column(Integer, index=True)
    machineStatus = Column(String(255), index=True)

class Bauf(Base):
    __tablename__ = "bauf"
    id = Column(Integer, primary_key=True, index=True)
    bauf_artnr = Column(Integer, index=True)
    bauf_artbez = Column(Integer, index=True)