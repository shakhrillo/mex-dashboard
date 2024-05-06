// pm2 start "uvicorn server.main:app --port=3231" --name "server-nfc"
// http://192.168.100.23:7878
module.exports = {
  apps: [
    {
      name: "server-nfc",
      script: "uvicorn",
      args: "server.main:app --port=7870",
    },
  ],
};