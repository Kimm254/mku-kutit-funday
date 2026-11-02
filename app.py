from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "HEAD"])
def home():
    return "MKU KUTIT FUNDAY WEBSITE IS WORKING!"

if __name__ == "__main__":
    app.run()
