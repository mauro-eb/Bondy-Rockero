from flask import (
  Flask,
  render_template,
)
import json

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('index.html', name='Elpi')