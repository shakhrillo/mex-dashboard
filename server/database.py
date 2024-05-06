from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# host="192.168.100.21",
#   user="qqdb_wweb",
#   password="M6p8xK7q1E",
#   database="schichtprotokoll"
# DB_URL = "mysql+pymysql://qqdb_wweb:M6p8xK7q1E@192.168.100.21:3306/schichtprotokoll"
# host="127.0.0.1",
#   user="root",
#   database="schichtprotokoll"
# DB_URL = "mysql+pymysql://new_user:password@127.0.0.1:3306/schichtprotokoll"
DB_URL = "mysql+pymysql://root@127.0.0.1:3306/schichtprotokoll"
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

DB_URL_2 = "mysql+pymysql://root@127.0.0.1:3306/alfaplus"
engine_2 = create_engine(DB_URL_2,echo=True)
SessionLocal_2 = sessionmaker(autocommit=False,autoflush=False, bind=engine_2)


# host="192.168.100.21",
# user="qqdb_wweb",
# password="M6p8xK7q1E",
# database="alfaplus"

# Base = declarative_base()

Base = declarative_base()
