module.exports = {
  apps : [{
    name: "server-nfc",
    script: "uvicorn",
    args: "server.main:app --port=3231",
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
