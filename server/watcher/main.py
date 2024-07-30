import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values
config = dotenv_values(".env")

print("Starting watcher...")

print(config["DB_HOST"])

# Email configuration
SMTP_SERVER = '192.168.100.47'
SMTP_PORT = 25
SMTP_USER = 'zmailer@ktbu.local'
SMTP_PASSWORD = 'Bc2Z05Xp0o'
TO_EMAIL = 'marco@ktbu.local'

# Function to send email
def send_email(article_no, article_name):
    print(f"Sending email for article {article_no} - {article_name}")
    # print(f"Sending email for article {article_no} - {article_name}")
    subject = f'Neuer Montageauftrag {article_name} erstellt'
    body = f"""
    Es wurde ein neuer Montageauftrag erstellt:

    Artikelnummer: {article_no}
    Artikelname: {article_name}

    Bitte die notwendigen Unterlagen zur Verfügung stellen.
    """

    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, TO_EMAIL, msg.as_string())

# Connect to the database
try:
    connection = mysql.connector.connect(
        host=config["DB_HOST"],
        database=config["DB_DATABASE"],
        user=config["DB_USERNAME"],
        password=config["DB_PASSWORD"],
        port=config["DB_PORT"]
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT id, bauf_artnr, bauf_artbez FROM email_notifications")
        rows = cursor.fetchall()

        for row in rows:
            id, article_no, article_name = row
            send_email(article_no, article_name)

            # After sending the email, delete the record
            cursor.execute("DELETE FROM email_notifications WHERE id = %s", (id,))
            connection.commit()

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
