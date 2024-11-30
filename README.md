# 🌟 **Monitor-Services Project** 🌟

### 🎯 **Purpose**
This project was developed to:
- ✅ **Monitor the status of Service1**:
  - Check if it is functioning properly (On/Off) and responds with the correct HTTP Status Code.
- ✅ **Simulate and test TLS/SSL issues**:
  - Test connectivity problems between Service1 and Service2.
- ✅ **Learn and understand multi-service systems**:
  - Use Flask to build APIs and UI.
  - Test the system using Postman.

---

## 🛠️ **Features**
### 📌 **Service1**
- UI with **Toggle Switch**:
  - Toggle the On/Off status of Service1.
  - Simulate TLS/SSL issues between Service1 and Service2.
- Respond with **HTTP Status Codes**:
  - `200 OK` for normal operations.
  - `500 Internal Server Error` when issues are simulated.

### 📌 **Service2**
- Accepts `idCard` data via API.
- Connects to Service1 and forwards HTTP Status Code and response message back to the client.
- Handles simulated errors from Service1 and forwards the issues accurately.

---

## 📂 **Project Structure**
```plaintext
Monitor-Services/
├── Service1/
│   ├── app.py               # Service1 Code
│   └── templates/
│       └── index.html       # UI for Service1
├── Service2/
│   └── app.py               # Service2 Code
└── README.md                # Project Documentation


🚀 Getting Started
1️⃣ Install Dependencies
python3 --version
pip3 install flask flask-cors
pip3 install requests
pip3 show requests

pip3 install flask flask-cors requests
pip3 install --upgrade pip

2️⃣ Run Service1
cd Service1
python3 app.py

Access the UI at http://localhost:5001 to toggle the status and simulate issues.

3️⃣ Run Service2
cd Service2
python3 app.py

4️⃣ Test with Postman
Send a POST request to:
POST http://localhost:5002/api/service2
Example Request Body:
json
{
    "idCard": "1234567890123"
}








