import flask
from waitress import serve
import WeatherManager as wman

localhost = flask.Flask(__name__)

@localhost.route('/get-weather', methods=['GET'])
def SendInfo():
    return wman.GetInfo(flask.request.args['city'])

@localhost.route("/close", methods=['POST'])
def CloseServer():
    func = flask.request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    return "Server Shutting down..."

if __name__ == '__main__':
    serve(localhost, listen='*:5000')