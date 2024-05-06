import os
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
config = dotenv_values(".env")

host = config["DB_HOST"]
port = config["DB_PORT"]
username = config["DB_USERNAME"]
password = config["DB_PASSWORD"]

DB_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/schichtprotokoll"
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

DB_URL_2 = f"mysql+pymysql://{username}:{password}@{host}:{port}/alfaplus"
engine_2 = create_engine(DB_URL_2,echo=True)
SessionLocal_2 = sessionmaker(autocommit=False,autoflush=False, bind=engine_2)

Base = declarative_base()
