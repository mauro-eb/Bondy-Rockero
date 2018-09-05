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


@app.route("/")
def hello():
    return render_template('index.html', name='Mala Fama')


@app.route('/artists/', methods=['GET'])
def get_artists():
    name = request.args.get('name')
    response = requests.get('https://www.evbqaapi.com/v3/artists/?token={token}&name_filter={name_filter}'.format(
            token=app.config["EB_API_KEY"],
            name_filter=name,
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


@app.route('/performances/', methods=['GET'])
def get_performances():
    artist_ids = request.args.get('artist_ids')
    contents = requests.get(
        'http://www.evbqaapi.com/v3/performances?token={token}&artist_ids={artist_ids}&expand={expand}'.format(
            token=app.config['EB_API_KEY'],
            artist_ids=artist_ids,
            expand='event,event.venue',
        ))
    return contents.text
