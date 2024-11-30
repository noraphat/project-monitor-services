from flask import Flask, jsonify, request, make_response
import requests

app = Flask(__name__)

@app.route('/api/service2', methods=['POST'])
def service2_api():
    # รับ idCard จาก Postman
    data = request.json
    id_card = data.get("idCard")

    try:
        # เรียก Service1 พร้อม Header User-Agent
        response = requests.get("http://localhost:5001/api", headers={"User-Agent": "Service2"})
        
        # Forward Response จาก Service1 โดยตรง
        return make_response(jsonify({
            "idCard": id_card,
            "service1_message": response.json()["message"]
        }), response.status_code)
    except requests.exceptions.RequestException as e:
        # กรณีที่ Service1 ไม่สามารถเชื่อมต่อได้
        return make_response(jsonify({
            "idCard": id_card,
            "service1_message": f"Error: {str(e)}"
        }), 500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
