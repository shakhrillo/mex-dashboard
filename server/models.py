from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    
    comment = Column(String(255), index=True)
    preparation_shift = Column(String(255), index=True)
    date = Column(Date, index=True)
    token = Column(ForeignKey("users.token"), index=True)
    shift = Column(String(255), index=True)

    user = relationship("User", back_populates="comments")

class StartMachine(Base):
    __tablename__ = "workflow"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(ForeignKey("users.token"), index=True)
    start_time = Column(Date, index=True)
    end_time = Column(Date, index=True)
    # shift = Column(String(255), index=True)

    user = relationship("User", back_populates="workflow")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    surname = Column(String(255), index=True)
    token = Column(String(255), index=True)

    machines = relationship("MachineData", back_populates="user")
    workflow = relationship("StartMachine", back_populates="user")
    comments = relationship("Comment", back_populates="user")

class Machine(Base):
    __tablename__ = "machines"
    machineQrCode = Column(String(255), primary_key=True, index=True)
    machine_data = relationship("MachineData", back_populates="machine")

class MachineData(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)

    machineQrCode = Column(String(255), ForeignKey("machines.machineQrCode"))
    token = Column(String(255), ForeignKey("users.token"))

    user = relationship("User", back_populates="machines")
    machine = relationship("Machine", back_populates="machine_data")

    shift = Column(String(255), index=True)
    createdAt = Column(String(255), index=True)
    toolMounted = Column(Boolean, index=True)
    machineStopped = Column(Boolean, index=True)
    barcodeProductionNo = Column(String(255), index=True)
    cavity = Column(Integer, index=True)
    cycleTime = Column(String(255), index=True)
    partStatus = Column(Boolean, index=True)
    pieceNumber = Column(Integer, index=True)
    note = Column(String(255), index=True)
    toolCleaning = Column(String(255), index=True)
    remainingProductionTime = Column(Integer, index=True)
    remainingProductionDays = Column(Integer, index=True)
    operatingHours = Column(Integer, index=True)
    machineStatus = Column(String(255), index=True)