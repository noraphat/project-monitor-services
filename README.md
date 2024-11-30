
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

## 📂 **Project Structure**
```plaintext
Monitor-Services/
├── CheckService/
│   ├── app.py               # Code for  Dashboard backend
│   ├── templates/
│   │   └── index.html       # UI for Dashboard backend
│   └── static/
│       └── styles.css       # Stylesheet for UI
├── Service1/
│   ├── app.py               # Code for Service1
│   ├── templates/
│   │   └── index.html       # UI for Service1
│   └── static/
│       └── styles.css       # Stylesheet for UI
├── Service2/
│   ├── app.py               # Code for Service2
├── README.md                # Project Documentation
```

---

## 🚀 **Getting Started**

### Prerequisites
- Python 3.x installed
- `pip` (Python package manager)

---

### 1️⃣ **Install Dependencies**
Install required libraries:
```bash
pip install flask flask-socketio requests
```

---

### 2️⃣ **Run Service1**
1. Navigate to the `Service1` directory:
   ```bash
   cd Service1
   ```
2. Start Service1:
   ```bash
   python app.py
   ```
3. Open your browser and go to:
   ```
   http://localhost:5001
   ```
   - Use the UI to toggle Service1 status and simulate TLS/SSL issues.

---

### 3️⃣ **Run Service2**
1. Navigate to the `Service2` directory:
   ```bash
   cd Service2
   ```
2. Start Service2:
   ```bash
   python app.py
   ```
3. Service2 will listen for API calls at:
   ```
   http://localhost:5002/api/service2
   ```

---

### 4️⃣ **Run the Dashboard**
1. From the main project directory:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://localhost:5005
   ```
3. The dashboard will update service statuses in real-time.

---

### 5️⃣ **Test the Services with Postman**
1. Open Postman and send a `POST` request to:
   ```
   POST http://localhost:5002/api/service2
   ```
2. Example Request Body:
   ```json
   {
       "idCard": "1234567890123"
   }
   ```
3. Observe the Response:
   - If Service1 **On** → HTTP 200 OK
   - If Service1 **Off** → HTTP 500 Internal Server Error
   - If TLS/SSL Issue is simulated → HTTP 500 Internal Server Error with appropriate message.

---

## 📸 **Features**
- **Service1**:
  - UI to manage the status (On/Off).
  - Simulate TLS/SSL issues between Service1 and Service2.
- **Service2**:
  - Accepts `idCard` from API and forwards responses from Service1.

---

## ✨ **Future Improvements**
- Add logging for better debugging.
- Support real TLS/SSL configurations.
- Integrate with a database for persistent data.
- Add unit tests for comprehensive testing.

---

💡 **Ready to Use!** Feel free to reach out for further queries 😊
