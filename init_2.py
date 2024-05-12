from dotenv import dotenv_values
import mysql.connector
config = dotenv_values(".env")

conn2 = mysql.connector.connect(
  host=config["DB_HOST"],
  user=config["DB_USERNAME"],
  password=config["DB_PASSWORD"],
  database="alfaplus"
)

cursor2 = conn2.cursor()

if config["DB_DEV"] == "True":
  cursor2.execute("DROP TABLE IF EXISTS bauf")
  cursor2.execute("CREATE TABLE IF NOT EXISTS bauf (id INT AUTO_INCREMENT PRIMARY KEY, bauf_artnr INT, bauf_artbez INT)")
  cursor2.execute("SELECT * FROM bauf")
  rows = cursor2.fetchall()

  if len(rows) == 0:
    cursor2.execute("INSERT INTO bauf (bauf_artnr, bauf_artbez) VALUES (80735, 001)") 
    conn2.commit()
    print("Data inserted successfully")

cursor2.execute("SELECT bauf.bauf_artnr AS Partnumber, bauf.bauf_artbez AS Partname FROM bauf WHERE bauf.bauf_aufnr = '811197' AND bauf.bauf_posnr = '001' LIMIT 1;")
rows = cursor2.fetchall()
print(rows)


cursor2.close()
conn2.close()

cursor.close()
conn.close()