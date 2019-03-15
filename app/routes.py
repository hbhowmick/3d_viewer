from app import app
from flask import render_template, url_for, redirect
from app.forms import LatLongForm, AddressForm


@app.route('/')
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form_LatLong = LatLongForm()
    if form_LatLong.validate_on_submit():
        lat = form_LatLong.lat.data
        long = form_LatLong.long.data
        return render_template('index.html', title='Home', form_LatLong=form_LatLong, lat=lat, long=long)

    form_Address = AddressForm()
    if form_Address.validate_on_submit():
        street = form_Address.street.data
        city = form_Address.city.data
        state = form_Address.state.data
        zip = int(form_Address.zip.data)
        return render_template('index.html', title='Home', form_Address=form_Address, street=street, city=city, state=state, zip=zip)

    return render_template('index.html', title='Home', form_LatLong=form_LatLong, form_Address=form_Address)

@app.route('/scene')
def scene():
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('scene.html', title='3D Scene')

@app.route('/tilt')
def tilt():
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('tilt.html', title='Tilted Scene')
