from dotenv import dotenv_values
import mysql.connector

from init.data import init_data
from init.user import init_user
config = dotenv_values(".env")

conn = mysql.connector.connect(
  host=config["DB_HOST"],
  user=config["DB_USERNAME"],
  password=config["DB_PASSWORD"],
  database="schichtprotokoll"
)

cursor = conn.cursor()

if config["DB_DEV"] == "True":
  init_user(cursor, conn)
  
# if config["DB_DEV"] == "True":
#   init_data(cursor, conn)

if config["DB_DEV"] == "True":
  cursor.close()
  conn.close()