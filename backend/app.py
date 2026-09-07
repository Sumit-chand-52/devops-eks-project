from flask import Flask, jsonify
from flask_cors import CORS
import socket
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/health')
def health():
	return jsonify({"status": "ok", "service": "backend"})

@app.route('/api/data')
def data():
	return jsonify({
"message": "Hello from the backend!",
"timestamp": datetime.datetime.utcnow().isoformat(),
"hostname": socket.gethostname()
})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
