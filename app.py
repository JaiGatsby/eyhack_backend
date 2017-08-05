#!flask/Scripts/python
from flask import Flask, jsonify, request, abort, make_response
import os
import NLP #import clean_eng, clean_chn, train, predict
import DB

app = Flask(__name__)

routes = [
    "GET /route1",
    "GET /route2",
]


@app.route('/', methods=['GET'])
def handleHome():
    """ Returns the available routes when a GET request is sent to '/'
    """
    return jsonify({'routes': routes})


@app.route('/classify', methods=['GET'])
def handleClassify():
    """ Description
        Parameters as URL query:
    """
    return jsonify({"Error":"Not Implemented"}), 501


@app.route('/train', methods=['GET'])
def handleTrain():
    """ Description
        Parameters as URL query:
    """
    return jsonify({"Error":"Not Implemented"}), 501

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'Error': "Please check with documentation to ensure correct syntax"}), 400)

if __name__ == '__main__':
    port = int(os.environ.get('PORT',8080))
    app.run(host = '0.0.0.0', debug=True, port=port)
