import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/predictor', methods=['POST'])
def makePrediction():
    movies = []
    for element in request.json:
        movies.append(predict(element['movieid'], element['number']))
    return jsonify(movies), 200


if __name__ == '__main__':
    app.run()  

