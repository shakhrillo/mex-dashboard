from dotenv import dotenv_values
import mysql.connector
config = dotenv_values(".env")

conn = mysql.connector.connect(
  host=config["DB_HOST"],
  user=config["DB_USERNAME"],
  password=config["DB_PASSWORD"],
  database="schichtprotokoll"
)

conn2 = mysql.connector.connect(
  host=config["DB_HOST"],
  user=config["DB_USERNAME"],
  password=config["DB_PASSWORD"],
  database="alfaplus"
)

cursor = conn.cursor()

cursor2 = conn2.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), token VARCHAR(255))")

cursor.execute("SELECT * FROM users WHERE username = 'admin'")
rows = cursor.fetchall()
print(len(rows))
if len(rows) == 0:
  cursor.execute("INSERT INTO users (username, token) VALUES ('admin', '0004650166692')") 
  conn.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS machines (id INT AUTO_INCREMENT PRIMARY KEY, token VARCHAR(255), machineQrCode VARCHAR(255), toolMounted BOOLEAN, machineMounted BOOLEAN, barcodeProductionNo VARCHAR(255), partNumber INT, partName INT, cavity INT, cycleTime VARCHAR(255), partStatus VARCHAR(255), pieceNumber INT, note VARCHAR(255), toolCleaning VARCHAR(255), remainingProductionTime INT, operatingHours INT, machineStatus VARCHAR(255))")

# {
#     "token": "0004650166692",
#     "machineQrCode": "F450iA–1",
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

# add above data to machines table
cursor.execute("SELECT * FROM machines")
rows = cursor.fetchall()

print(len(rows))

if len(rows) == 0:
  cursor.execute("INSERT INTO machines (token, machineQrCode, toolMounted, machineMounted, barcodeProductionNo, partNumber, partName, cavity, cycleTime, partStatus, pieceNumber, note, toolCleaning, remainingProductionTime, operatingHours, machineStatus) VALUES ('0004650166692', 'F450iA–1', true, true, '0004650166692', 123456, 123, 1, '2,3', 'Good', 1, 'Note', '3,2', 0, 0, 'completed')") 
  conn.commit()
  print("Data inserted successfully")


# create bauf table
cursor2.execute("CREATE TABLE IF NOT EXISTS bauf (id INT AUTO_INCREMENT PRIMARY KEY, bauf_artnr INT, bauf_artbez INT)")

# add data to bauf table
cursor2.execute("SELECT * FROM bauf")
rows = cursor2.fetchall()

print(len(rows))

if len(rows) == 0:
  cursor2.execute("INSERT INTO bauf (bauf_artnr, bauf_artbez) VALUES (80735, 001)") 
  conn2.commit()
  print("Data inserted successfully")

cursor2.close()
conn2.close()

cursor.close()
conn.close()