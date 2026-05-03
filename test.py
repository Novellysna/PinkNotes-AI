from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello defri"

if __name__ == "__main__":
    print("TEST SERVER: http://127.0.0.1:5055")
    app.run(
        host="127.0.0.1",
        port=5055,
        debug=False
    )