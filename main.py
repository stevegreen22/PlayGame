from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "index!"


@app.route("/members")
def members():
    return "Members"


@app.route("/members/<name>/")
def getMember(name):
    return name


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
