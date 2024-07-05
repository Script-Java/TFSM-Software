from flask import Flask
from flask_cors import CORS
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apidb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'e5b53eacd3d3498f91b4d872c89d2d3c'

CORS(app)
db.init_app(app)

import routes

#with app.app_context():
#    db.create_all()

if __name__ == '__main__':

  app.run(host='0.0.0.0', port=5000)
