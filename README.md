# El Bondi Rockero

1. Install a python env with python 3.5
2. Install Flask library
```
pip install flask
```
3. Export vars in order to run our app
```
# Indicate the app
export FLASK_APP=app.py
# Indicate that is under development mode
export FLASK_ENV=development
# Indicate flask to reload automatically
export FLASK_DEBUG=1
# Make templates render every time
export TEMPLATES_AUTO_RELOAD=True
```
4. run the app
```
flask run
```