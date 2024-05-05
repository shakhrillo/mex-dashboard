import mysql.connector

conn = mysql.connector.connect(
  # mysql+pymysql://new_user:password@127.0.0.1:3306/schichtprotokoll
  host="127.0.0.1",
  user="new_user",
  password="password",
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



cursor.close()
conn.close()