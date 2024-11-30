from flask import Flask, render_template
from flask_socketio import SocketIO
import requests
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

# Function to fetch service status
def check_service_status(url, payload):
    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            return {"status": "active", "message": response.json().get("message", "No message")}
        else:
            return {"status": "down", "message": response.json().get("message", "No message")}
    except Exception as e:
        return {"status": "down", "message": str(e)}

# Background thread to fetch and emit service statuses
def fetch_and_emit_status():
    while True:
        squads = [
            {
                "name": "Squad 1",
                "services": [
                    {"name": "Service1", "url": "http://localhost:5001/api", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}}
                ]
            },
            {
                "name": "Squad 2",
                "services": [
                    {"name": "Service1", "url": "http://localhost:5001/api", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}},
                    {"name": "Service2", "url": "http://localhost:5002/api/service2", "payload": {"idCard": "1234567890123"}}
                ]
            }
        ]

        for squad in squads:
            for service in squad["services"]:
                status_info = check_service_status(service["url"], service["payload"])
                service["status"] = status_info["status"]
                service["message"] = status_info["message"]

        # Emit the updated data to all connected clients
        socketio.emit("update_status", {"squads": squads})
        time.sleep(5)  # Fetch every 5 seconds

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Start the background thread
    thread = threading.Thread(target=fetch_and_emit_status)
    thread.daemon = True
    thread.start()

    # Run the Flask-SocketIO server on port 5005
    socketio.run(app, host="0.0.0.0", port=5005, debug=True)
