from flask import Flask, jsonify, render_template, request
import threading

app = Flask(__name__)
status = {"on": True}  # Toggle On/Off
simulate_tls_issue = {"enabled": False}  # Toggle TLS/SSL Issue

@app.route('/')
def index():
    return render_template('index.html', status=status["on"], simulate_tls_issue=simulate_tls_issue["enabled"])

@app.route('/toggle', methods=['POST'])
def toggle_status():
    status["on"] = not status["on"]
    return jsonify({"status": "success", "on": status["on"]})

@app.route('/simulate_tls', methods=['POST'])
def toggle_tls_issue():
    simulate_tls_issue["enabled"] = not simulate_tls_issue["enabled"]
    return jsonify({"status": "success", "simulate_tls_issue": simulate_tls_issue["enabled"]})

@app.route('/api', methods=['GET'])
def service1_api():
    # หาก Service1 ถูกปิด
    if not status["on"]:
        return jsonify({"message": "Service1 is down"}), 500

    # หากเปิดการจำลอง TLS/SSL Issue
    if simulate_tls_issue["enabled"] and request.headers.get("User-Agent") == "Service2":
        return jsonify({"message": "TLS/SSL issue simulated"}), 500

    # Service1 ทำงานปกติ
    return jsonify({"message": "Service1 is OK"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
