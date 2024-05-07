from dotenv import dotenv_values
import mysql.connector
config = dotenv_values(".env")

conn = mysql.connector.connect(
  host=config["DB_HOST"],
  user=config["DB_USERNAME"],
  password=config["DB_PASSWORD"],
  database="schichtprotokoll"
)

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), token VARCHAR(255))")

cursor.execute("SELECT * FROM users WHERE surname = 'admin'")
rows = cursor.fetchall()
print(len(rows))
if len(rows) == 0:
  cursor.execute("INSERT INTO users (name, surname, token) VALUES ('admin', 'admin', '0004650166692')")
  conn.commit()

cursor.execute("DROP TABLE IF EXISTS data")
# Add above data to the table
cursor.execute("CREATE TABLE IF NOT EXISTS data (id INT AUTO_INCREMENT PRIMARY KEY, createdAt VARCHAR(255), shift VARCHAR(255), token VARCHAR(255), machineQrCode VARCHAR(255), toolMounted BOOLEAN, machineMounted BOOLEAN, barcodeProductionNo VARCHAR(255), cavity INT, cycleTime INT, partStatus VARCHAR(255), pieceNumber INT, note VARCHAR(255), toolCleaning VARCHAR(255), remainingProductionTime INT, remainingProductionDays INT, operatingHours INT, machineStatus VARCHAR(255))")

cursor.execute("SELECT * FROM data")
rows = cursor.fetchall()

if len(rows) == 0:
  cursor.execute("INSERT INTO data (createdAt, shift, token, machineQrCode, toolMounted, machineMounted, barcodeProductionNo, cavity, cycleTime, partStatus, pieceNumber, note, toolCleaning, remainingProductionTime, remainingProductionDays, operatingHours, machineStatus) VALUES ('2021-09-01 00:00:00', '1', '0004650166692', '0004650166692', 1, 1, '0004650166692', 1, 8, 'OK', 1, 'OK', 'OK', 0, 0, 0, 'OK')")
  conn.commit()
  print("Data inserted successfully")

conn2 = mysql.connector.connect(
  host=config["DB_HOST"],
  user=config["DB_USERNAME"],
  password=config["DB_PASSWORD"],
  database="alfaplus"
)

# cursor2 = conn2.cursor()
# cursor2.execute("DROP TABLE IF EXISTS bauf")
# cursor2.execute("CREATE TABLE IF NOT EXISTS bauf (id INT AUTO_INCREMENT PRIMARY KEY, bauf_artnr INT, bauf_artbez INT)")
# cursor2.execute("SELECT * FROM bauf")
# rows = cursor2.fetchall()

# if len(rows) == 0:
#   cursor2.execute("INSERT INTO bauf (bauf_artnr, bauf_artbez) VALUES (80735, 001)") 
#   conn2.commit()
#   print("Data inserted successfully")

# cursor2.close()
# conn2.close()

cursor.close()
conn.close()