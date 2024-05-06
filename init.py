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

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), token VARCHAR(255))")

cursor.execute("SELECT * FROM users WHERE username = 'admin'")
rows = cursor.fetchall()
print(len(rows))
if len(rows) == 0:
  cursor.execute("INSERT INTO users (username, token) VALUES ('admin', '0004650166692')") 
  conn.commit()

# drop table machines
cursor.execute("DROP TABLE IF EXISTS machines")

cursor.execute("CREATE TABLE IF NOT EXISTS machines (id INT AUTO_INCREMENT PRIMARY KEY, token VARCHAR(255), machineQrCode VARCHAR(255), toolMounted BOOLEAN, machineMounted BOOLEAN, barcodeProductionNo VARCHAR(255), cavity INT, cycleTime VARCHAR(255), partStatus VARCHAR(255), pieceNumber INT, note VARCHAR(255), toolCleaning VARCHAR(255), remainingProductionTime INT, operatingHours INT, machineStatus VARCHAR(255))")

# add above data to machines table
cursor.execute("SELECT * FROM machines")
rows = cursor.fetchall()

if len(rows) == 0:
  cursor.execute("INSERT INTO machines (token, machineQrCode, toolMounted, machineMounted, barcodeProductionNo, cavity, cycleTime, partStatus, pieceNumber, note, toolCleaning, remainingProductionTime, operatingHours, machineStatus) VALUES ('0004650166692', 'F450iA-1', 1, 1, '80735001', 1, '00:00:00', 'OK', 0, 'OK', 'OK', 0, 0, 'OK')")
  conn.commit()
  print("Data inserted successfully")

conn2 = mysql.connector.connect(
  host=config["DB_HOST"],
  user=config["DB_USERNAME"],
  password=config["DB_PASSWORD"],
  database="alfaplus"
)

cursor2 = conn2.cursor()
# drop table bauf
cursor2.execute("DROP TABLE IF EXISTS bauf")
cursor2.execute("CREATE TABLE IF NOT EXISTS bauf (id INT AUTO_INCREMENT PRIMARY KEY, bauf_artnr INT, bauf_artbez INT)")
cursor2.execute("SELECT * FROM bauf")
rows = cursor2.fetchall()

if len(rows) == 0:
  # http://34.31.212.138/api/machines/F450iA-1/status
  cursor2.execute("INSERT INTO bauf (bauf_artnr, bauf_artbez) VALUES (80735, 001)") 
  conn2.commit()
  print("Data inserted successfully")

cursor2.close()
conn2.close()

cursor.close()
conn.close()