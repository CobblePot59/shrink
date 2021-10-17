from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from hashids import Hashids
import os
import validators

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/urls.db'
app.config['SECRET_KEY'] = '21359bb385cfb332aaedad6bee7cfc67983dde66143ee9c7ac0cdda204d4474d'

db = SQLAlchemy(app)
hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])
from models import *


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        url = request.form['url']

        if not validators.url(url):
            flash('A valid URL is required!', 'danger')
            return redirect(url_for('index'))

        url_data = Urls(original_url = url)
        db.session.add(url_data)
        db.session.commit()

        short_url = os.getenv('URL') + hashids.encode(url_data.id)
        return render_template('index.html', short_url=short_url)
    else:
        return render_template('index.html')


@app.route('/<id>')
def url_redirect(id):
    original_id = hashids.decode(id)
    if original_id:
        original_id = original_id[0]
        url_data = Urls.query.filter_by(id=original_id).first()
        
        url_data.clicks = url_data.clicks+1
        db.session.commit()
        
        original_url = url_data.original_url
        return redirect(original_url)
    else:
        return 'Not Found'

@app.route('/stats')
def stats():
    urls = []
    db_urls = Urls.query.all()
    for obj in db_urls:
       url = obj.__dict__
       url['short_url'] = os.getenv('URL') + hashids.encode(url['id'])
       urls.append(url)
    return render_template('stats.html', urls=urls)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
