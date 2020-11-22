import flask, json, torch
from random import Random
from flask import request, jsonify
from fastai.tabular.all import *
from fastai.collab import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

learn = load_learner('./ratings_model(1).pkl')
def predict(userId, movieId):
    return learn.model(tensor([[userId, movieId]])).item()

@app.route('/api/predictor', methods=['POST'])
def makePrediction():
    movies = dict()
    body = json.loads(request.json)
    for element in body:
        user = body[element]["userId"]
        movie = body[element]["movieId"]
        movies[element] = predict(user, movie)
    return jsonify(movies), 200


if __name__ == '__main__':
    app.run()  

