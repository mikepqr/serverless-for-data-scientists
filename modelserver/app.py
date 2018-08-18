import pickle

import requests
from flask import Flask, request

app = Flask(__name__)

url = "https://s3.amazonaws.com/modelservingdemo/classifier.pkl"
r = requests.get(url)
classifier = pickle.loads(r.content)


@app.route("/predict")
def predict():
    X = [[float(request.args['feature_1']),
          float(request.args['feature_2'])]]
    label = classifier.predict(X)
    if label == 0:
        return 'purple blob'
    else:
        return 'yellow blob'


if __name__ == "__main__":
    app.run()
