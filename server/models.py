from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), index=True)
    token = Column(String(255), index=True)
class Machine(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(255), index=True)
    machineQrCode = Column(String(255), index=True)
    toolMounted = Column(Boolean, index=True)
    machineMounted = Column(Boolean, index=True)
    barcodeProductionNo = Column(String(255), index=True)
    partNumber = Column(Integer, index=True)
    partName = Column(Integer, index=True)
    # cavity must be in input field between 1-99
    cavity = Column(Integer, index=True)
    cycleTime = Column(String(255), index=True)
    partStatus = Column(String(255), index=True)
    # between 1-1.000.000 ( no , or . allowed)
    pieceNumber = Column(Integer, index=True)
    note = Column(String(255), index=True)
    toolCleaning = Column(String(255), index=True)
    remainingProductionTime = Column(Integer, index=True)
    operatingHours = Column(Integer, index=True)
    machineStatus = Column(String(255), index=True)
    
# CREATE TABLE IF NOT EXISTS data (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     token VARCHAR(255),
#     machineQrCode VARCHAR(255),
#     toolMounted BOOLEAN,
#     machineMounted BOOLEAN,
#     barcodeProductionNo VARCHAR(255),
#     partNumber INT,
#     partName INT,
#     cavity INT,
#     cycleTime VARCHAR(255),
#     partStatus VARCHAR(255),
#     pieceNumber INT,
#     note VARCHAR(255),
#     toolCleaning VARCHAR(255),
#     remainingProductionTime INT,
#     operatingHours INT
# )

# {
#     "token": "0004650166692",
#     "machineQrCode": "F 450iA – 1",
#     "toolMounted": true,
#     "machineMounted": true,
#     "barcodeProductionNo": "0004650166692",
#     "partNumber": 123456,
#     "partName": 123,
#     "cavity": 1,
#     "cycleTime": "2,3",
#     "partStatus": "Good",
#     "pieceNumber": 1,
#     "note": "Note",
#     "toolCleaning": "3,2",
#     "remainingProductionTime": 0,
#     "operatingHours": 0,
#     "machineStatus": "completed"
# }