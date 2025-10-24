#Python Application
from flask import Flask


app = Flask(__name__)


@app.get("/")
def hello():
return "Hello, World! This is a simple Python app for Jenkins Project", 200


if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000)