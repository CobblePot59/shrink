from flask import render_template, request, flash, redirect, url_for
from app import app, db, hashids
from app import Urls
import os
import validators

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
