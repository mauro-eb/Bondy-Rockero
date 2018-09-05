from flask import (
    Flask,
    jsonify,
    render_template,
)
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html', name='Elpi')


@app.route('/artists/', methods=['GET'])
def get_artists():
    return jsonify([
        {
            'artist_id': 1,
            'name': 'nombre',
        }
    ])


@app.route('/artists/<int:artist_id>/', methods=['GET'])
def get_artist(artist_id):
    return jsonify({
        'artist_id': artist_id,
        'name': 'nombre',
      })
