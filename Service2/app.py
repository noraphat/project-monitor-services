from flask import Flask, jsonify, request, make_response
import requests

app = Flask(__name__)

@app.route('/api/service2', methods=['POST'])  # รองรับ POST เท่านั้น
def service2_api():
    # รับ idCard จาก JSON
    try:
        data = request.get_json()
        id_card = data.get("idCard")
        if not id_card:
            return jsonify({"error": "idCard is required"}), 400
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    try:
        # เรียก Service1 ด้วย Method POST พร้อม JSON Body
        response = requests.post(
            "http://localhost:5001/api",
            json={"idCard": id_card},
            headers={"User-Agent": "Service2"}  # ตั้ง User-Agent เป็น Service2
        )

        # หาก Service1 ทำงานปกติ
        if response.status_code == 200:
            return make_response(jsonify({
                "idCard": id_card,
                "service1_message": response.json().get("message")
            }), 200)

        # หาก Service1 อยู่ในสถานะ Down หรือจำลอง TLS Issue
        else:
            return make_response(jsonify({
                "service1_message": response.json().get("message")
            }), response.status_code)
    except requests.exceptions.RequestException as e:
        # กรณีที่ Service1 ไม่สามารถเชื่อมต่อได้
        return make_response(jsonify({
            "service1_message": f"Error: {str(e)}"
        }), 500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
