from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class LatLongForm(FlaskForm):
    lat = StringField('Latitude: ')
    long = StringField('Longitude: ')
    submit_LatLong = SubmitField('Submit')

class AddressForm(FlaskForm):
    street = StringField('Street Address: ')
    city = StringField('City: ')
    state = StringField('State: ')
    zip = IntegerField('Zip: ')
    submit_Address = SubmitField('Submit')
