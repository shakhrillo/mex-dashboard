from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# DB Name> schichtprotokoll
# DB User> qqdb_wweb
# DB Password> M6p8xK7q1E
# SB SERVER IP 192.168.100.21
# host="127.0.0.1",
#   user="root",
#   database="schichtprotokoll"
# DB_URL = "mysql+pymysql://new_user:password@127.0.0.1:3306/schichtprotokoll"
DB_URL = "mysql+pymysql://root@127.0.0.1:3306/schichtprotokoll"
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()
