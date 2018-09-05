from flask import (
    Flask,
    render_template,
    request,
)
import requests
import app
import json


app = Flask(__name__)
app.config.from_pyfile('config.py')


def get_artists(name):
    response = requests.get('https://www.evbqaapi.com/v3/artists/?token={token}&name={name}'.format(
            token=app.config["EB_API_KEY"],
            name=name,
        )
    )
    return response.content


@app.route('/artists/<int:artist_id>/', methods=['GET'])
def get_artist(artist_id):
    response = requests.get('https://www.evbqaapi.com/v3/artists/{artist_id}/?token={token}'.format(
            artist_id=artist_id,
            token=app.config["EB_API_KEY"],
        )
    )
    return response.text


@app.route('/performances/', methods=['GET'])
def get_performances():
    artist_name = request.args.get('name')
    artist = json.loads(get_artists(artist_name))
    artist_id = artist.get('artists')[0].get('id')
    contents = requests.get(
        'http://www.evbqaapi.com/v3/performances?token={token}&artist_ids={artist_ids}&expand={expand}'.format(
            token=app.config['EB_API_KEY'],
            artist_ids=artist_id,
            expand='event,event.venue',
        ))
    return contents.text
