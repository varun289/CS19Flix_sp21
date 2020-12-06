import flask, json, torch
from flask_cors import CORS
from random import Random
from flask import request, jsonify
from fastai.tabular.all import *
from fastai.collab import *

app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = False

learn = load_learner('./ratings_model(1).pkl')
def predict(userId, movieId):
    return learn.model(tensor([[userId, movieId]])).item()

@app.route('/api/predictor', methods=['POST'])
def makePrediction():
    movies = dict()
    body = request.json
    user = body["userId"]
    movie = body["movieId"]
    movies["rating"] = round(predict(user, movie), 1)
    return jsonify(movies), 200


if __name__ == '__main__':
    app.run()

