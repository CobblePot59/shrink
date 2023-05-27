from app import app, db
from datetime import datetime


now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    original_url = db.Column(db.String(255), nullable=False)
    clicks = db.Column(db.Integer, nullable=False, default=0)

with app.app_context():
    db.create_all()
