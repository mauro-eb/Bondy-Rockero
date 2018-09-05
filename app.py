from flask import (
    Flask,
    render_template,
)
import requests
import os
import jsonify

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/artists/', methods=['GET'])
def get_artists():
    response = requests.get('https://www.evbqaapi.com/v3/artists/?token={token}&expand=extended_data'.format(
            token=os.environ["EB_API_KEY"],
        )
    )
    return response.content


@app.route('/artists/<int:artist_id>/', methods=['GET'])
def get_artist(artist_id):
    response = requests.get('https://www.evbqaapi.com/v3/artists/{artist_id}/?token={token}&expand=extended_data'.format(
            artist_id=artist_id,
            token=os.environ["EB_API_KEY"],
        )
    )
    return response.content


@app.route('/status/', methods=['GET'])
def get_status():
    return jsonify([
        {
            'api_key': app.config['EB_API_KEY'],
            'jok': 2
        }
    ])
