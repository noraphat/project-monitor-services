
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
├── Service1/
│   ├── app.py               # Service1 Code
│   └── templates/
│       └── index.html       # UI for Service1
├── Service2/
│   └── app.py               # Service2 Code
└── README.md                # Project Documentation
```

---

## 🚀 **Getting Started**

### Prerequisites
- Python 3.x installed
- `pip` (Python package manager)

### 1️⃣ **Install Dependencies**
Install required libraries:
```bash
pip3 install flask flask-cors requests
```

---

### 2️⃣ **Run Service1**
1. Navigate to the `Service1` directory:
   ```bash
   cd Service1
   ```
2. Start the service:
   ```bash
   python3 app.py
   ```
3. Open your browser and go to:
   ```
   http://localhost:5001
   ```
   - Use the **UI Toggle** to manage the status of Service1 and simulate TLS/SSL issues.

---

### 3️⃣ **Run Service2**
1. Navigate to the `Service2` directory:
   ```bash
   cd Service2
   ```
2. Start the service:
   ```bash
   python3 app.py
   ```
3. Service2 will listen for API calls on:
   ```
   http://localhost:5002/api/service2
   ```

---

### 4️⃣ **Test the Services with Postman**
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
   - If Service1 is **On** and no TLS/SSL issue → HTTP 200 OK
   - If Service1 is **Off** → HTTP 500 Internal Server Error
   - If TLS/SSL issue is simulated → HTTP 500 Internal Server Error with appropriate message.

---

## 📸 **Screenshots**
### Service1 UI
![Service1 UI](https://via.placeholder.com/800x400.png?text=Service1+UI+Example)

---

### Postman Example
Response when `TLS/SSL Issue = ON`:
```json
{
    "idCard": "1234567890123",
    "service1_message": "TLS/SSL issue simulated"
}
```

---

## 🌟 **Features**
- Service1:
  - Toggle to manage On/Off status.
  - Simulate TLS/SSL issues between services.
- Service2:
  - Accepts `idCard` from API.
  - Forwards HTTP Status Code and messages from Service1 to the client.

---

## 🌟 **Future Improvements**
- Add logging for better debugging and monitoring.
- Support real TLS/SSL configurations for secure connections.
- Integrate with a database for persistent data.
- Write unit tests for comprehensive testing.

---

## ✨ **Why This Project?**
This project serves as a learning experience for:
1. Building a multi-service architecture.
2. Debugging and simulating network issues.
3. Understanding API testing workflows with Postman.

---

💡 **Ready to Use!** Feel free to ask for further customization or enhancements 😊
