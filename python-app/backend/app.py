from flask import Flask

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}! This is the backend."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
