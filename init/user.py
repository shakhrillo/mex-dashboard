def init_user(cursor, conn):
  cursor.execute("DROP TABLE IF EXISTS users")
  cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), token VARCHAR(255))")
  cursor.execute("SELECT * FROM users WHERE surname = 'admin'")
  rows = cursor.fetchall()
  if len(rows) == 0:
    cursor.execute("INSERT INTO users (name, surname, token) VALUES ('admin', 'admin', '0004650166692')")
    conn.commit()