<!-- uvicorn server.main:app --reload --port=5000 -->

pm2 start "uvicorn server.main:app --port=3231" --name "server-nfc"

[
    {
        "name": "F450iA-1",
        "status": "running"
    },
    {
        "name": "E 35-1",
        "status": "stopped"
    },
    {
        "name": "E 45-2",
        "status": "running"
    },
    {
        "name": "E 45-1",
        "status": "running"
    },
    {
        "name": "E 50-2",
        "status": "running"
    },
    {
        "name": "E 50-3",
        "status": "running"
    },
    {
        "name": "Emac50-1",
        "status": "running"
    },
    {
        "name": "Emac50-2",
        "status": "running"
    },
    {
        "name": "Emac50-3",
        "status": "running"
    },
    {
        "name": "F150iA-1",
        "status": "running"
    },
    {
        "name": "E 80-1",
        "status": "running"
    },
    {
        "name": "E 120-1",
        "status": "running"
    },
    {
        "name": "E 55-1",
        "status": "running"
    },
    {
        "name": "KM 150-1",
        "status": "running"
    },
    {
        "name": "KM 80-1",
        "status": "running"
    },
    {
        "name": "KM 50-1",
        "status": "running"
    },
    {
        "name": "KM 420-1",
        "status": "running"
    },
    {
        "name": "F250iA-1",
        "status": "running"
    }
]

{
    "title": "string",
    "partName": "F150iA-1",
    "date": "03 May 2024 - Friday",
    "time": 12,
    "type": "active"
}


-- Create the logging table
CREATE TABLE email_notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bauf_artnr VARCHAR(255),
    bauf_artbez VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the trigger
DELIMITER //

CREATE TRIGGER after_insert_bauf
AFTER INSERT ON bauf
FOR EACH ROW
BEGIN
    IF NEW.bauf_posnr = 2 THEN
        INSERT INTO email_notifications (bauf_artnr, bauf_artbez)
        VALUES (NEW.bauf_artnr, NEW.bauf_artbez);
    END IF;
END//

DELIMITER ;
