import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/time")
def time():
    return str(datetime.datetime.now())


if __name__ == "__main__":
    app.run()
