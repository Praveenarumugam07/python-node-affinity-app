from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Backend service URL (will be Kubernetes service name)
BACKEND_URL = "http://backend-svc:5001"

@app.route("/")
def home():
    return "Welcome to Frontend! Go to /api?name=YourName to call backend."

@app.route("/api")
def api():
    name = request.args.get("name", "Guest")
    try:
        response = requests.get(f"{BACKEND_URL}/hello/{name}")
        return f"Frontend -> {response.text}"
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
