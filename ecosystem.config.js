
// pm2 start "uvicorn server.main:app --port=3231" --name "server-nfc"
module.exports = {
  apps : [{
    name: "server-nfc",
    args: "uvicorn server.main:app --port=7878",
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'production'
    },
    interpreter: "/home/qqtechx/nfc_dash/myenv/bin/python"
  }]
}
