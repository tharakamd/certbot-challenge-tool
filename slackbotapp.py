from io import BytesIO

from flask import Flask, send_file, request, abort, jsonify, Response
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

import swagger

app = Flask(__name__)
CORS(app)

challenges = {}


@app.errorhandler(400)
def custom400(error):
    return jsonify({'message': error.description})


@app.route('/challenges', methods=['POST'])
def create_challenge():
    if not request.json:
        abort(400)

    json = request.json
    challenge_id = ''
    challenge_content = ''

    try:
        challenge_id = json['challenge_id']
    except:
        abort(400, 'challenge_id not found')

    try:
        challenge_content = json['challenge_content']
    except:
        abort(400, 'challenge_content not found ')

    challenges[challenge_id] = challenge_content

    return Response(response='{"message": "challenge added"}', status=201, mimetype='application/json')


@app.route('/challenges')
def get_challenges():
    return jsonify(challenges)


@app.route('/.well-known/acme-challenge/<challenge_id>')
def get_challenge_file(challenge_id):
    if challenge_id in challenges:
        print(challenge_id)
    else:
        abort(403, 'invalid challenge id')

    buffer = BytesIO()
    buffer.write(challenges[challenge_id].encode())
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, attachment_filename='challenge', mimetype='text/csv')


@app.route('/v2')
def get_swagger_json():
    return jsonify(swagger.swagger_json)


SWAGGER_URL = '/api/docs'
API_URL = 'http://localhost:5000/v2'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, )
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
