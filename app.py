from flask import Flask, jsonify
import os
import socket
from datetime import datetime
APP_VERSION = "3.1.1"

app = Flask(__name__)

@app.route("/")
def home():
       message = os.getenv("APP_MESSAGE", "DevOps Demo App Running")
       mode = os.getenv("APP_MODE", "dev")

       return jsonify({
           "message": message,
           "mode": mode,
           "hostname": socket.gethostname(),
           "timestamp": str(datetime.now())
       })

@app.route("/app")
def app_home():
    return home()

@app.route("/health")
def health():
        return jsonify({"status": "healthy"}), 200

@app.route("/version")
def version():
        return jsonify({"version": APP_VERSION}), 200

@app.route("/info")
def info():
    return jsonify({
        "application": "devops-project-v2",
        "version": APP_VERSION,
        "mode": os.getenv("APP_MODE", "dev")
    })

@app.route("/burn")
def burn():
    total = 0

    for i in range(30000000):
        total += i * i

    return jsonify({
        "status": "cpu burn complete",
        "result": total
    }), 200


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
