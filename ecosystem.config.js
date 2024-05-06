// pm2 start "uvicorn server.main:app --port=3231" --name "server-nfc"
// http://192.168.100.23:7878
// http://192.168.100.23:7878/api/machines/F450iA–1/status
module.exports = {
  apps: [
    {
      name: "server-nfc",
      script: "myenv/bin/uvicorn",
      args: "server.main:app --port=7870",
    },
  ],
};