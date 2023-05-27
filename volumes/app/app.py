from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashids import Hashids

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
from models import *

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

from views import *

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
