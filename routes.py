from flask.templating import render_template
from main import app

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/fetch')
def apifetch():
  return {'Fetching: Data'}

@app.route('api/return')
def apisend():
  return {'resturn data'}