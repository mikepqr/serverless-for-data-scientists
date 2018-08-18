import datetime
import pytz

from flask import Flask, request

app = Flask(__name__)


@app.route("/servertime")
def servertime():
    return str(datetime.datetime.now())


@app.route("/localtime")
def localtime():
    tz = pytz.timezone(request.args['tz'])
    servertime = datetime.datetime.now().astimezone()
    localtime = servertime.astimezone(tz)
    return str(localtime)


if __name__ == "__main__":
    app.run()
