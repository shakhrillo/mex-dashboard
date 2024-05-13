def init_data(cursor, conn):
  cursor.execute("DROP TABLE IF EXISTS data")
  print("Table dropped successfully")

  cursor.execute("CREATE TABLE IF NOT EXISTS data (id INT AUTO_INCREMENT PRIMARY KEY, createdAt VARCHAR(255), shift VARCHAR(255), token VARCHAR(255), machineQrCode VARCHAR(255), toolMounted BOOLEAN, machineMounted BOOLEAN, barcodeProductionNo VARCHAR(255), cavity INT, cycleTime INT, partStatus VARCHAR(255), pieceNumber INT, note VARCHAR(255), toolCleaning VARCHAR(255), remainingProductionTime INT, remainingProductionDays INT, operatingHours INT)")

  cursor.execute("SELECT * FROM data")
  rows = cursor.fetchall()

  if len(rows) == 0:
    cursor.execute("INSERT INTO data (createdAt, shift, token, machineQrCode, toolMounted, machineMounted, barcodeProductionNo, cavity, cycleTime, partStatus, pieceNumber, note, toolCleaning, remainingProductionTime, remainingProductionDays, operatingHours) VALUES ('2021-09-01 00:00:00', '1', '0004650166692', '0004650166692', 1, 1, '0004650166692', 1, 8, 'OK', 1, 'OK', 'OK', 0, 0, 0)")
    conn.commit()
    print("Data inserted successfully")