from flask import Flask, render_template
import requests

app = Flask(__name__)

# Function to check the status of a service
def check_service_status(url, payload):
    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            return {"status": "active", "message": response.json().get("message", "No message")}
        else:
            return {"status": "down", "message": response.json().get("message", "No message")}
    except Exception as e:
        return {"status": "down", "message": str(e)}

@app.route("/")
def dashboard():
    # Groups of services by Squad
    squads = [
        {
            "name": "Squad 1",
            "services": [
                {
                    "name": "Service1",
                    "url": "http://localhost:5001/api",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service2",
                    "url": "http://localhost:5002/api/service2",
                    "payload": {"idCard": "1234567890123"}
                }
            ]
        },
        {
            "name": "Squad 2",
            "services": [
                {
                    "name": "Service1",
                    "url": "http://localhost:5001/api",
                    "payload": {"idCard": "1234567890123"}
                },
                {
                    "name": "Service1",
                    "url": "http://localhost:5001/api",
                    "payload": {"idCard": "1234567890123"}
                }
            ]
        }
    ]

    # Check statuses for each service in all squads
    for squad in squads:
        for service in squad["services"]:
            status_info = check_service_status(service["url"], service["payload"])
            service["status"] = status_info["status"]
            service["message"] = status_info["message"]

    return render_template("index.html", squads=squads)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)
