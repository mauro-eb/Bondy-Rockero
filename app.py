from flask import (
    Flask,
    render_template,
)
import requests
import app
import jsonify

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/artists/', methods=['GET'])
def get_artists():
    response = requests.get('https://www.evbqaapi.com/v3/artists/?token={token}'.format(
            token=app.config["EB_API_KEY"],
        )
    )
    return response.text


@app.route('/artists/<int:artist_id>/', methods=['GET'])
def get_artist(artist_id):
    response = requests.get('https://www.evbqaapi.com/v3/artists/{artist_id}/?token={token}'.format(
            artist_id=artist_id,
            token=app.config["EB_API_KEY"],
        )
    )
    return response.text


@app.route('/status/', methods=['GET'])
def get_status():
    return jsonify([
        {
            'api_key': app.config['EB_API_KEY'],
            'jok': 2
        }
    ])
