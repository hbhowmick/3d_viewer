from app import app
from flask import render_template, url_for, redirect
from app.forms import ZoomForm


@app.route('/')
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ZoomForm()

    if form.validate_on_submit():
        lat = form.lat.data
        long = form.long.data
        return redirect(url_for('scene', lat=lat, long=long))

    return render_template('index.html', title='Home', form=form)

@app.route('/scene')
def scene():
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('scene.html', title='3D Scene')

@app.route('/tilt')
def tilt():
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('tilt.html', title='Tilted Scene')
