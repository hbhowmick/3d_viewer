from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ZoomForm(FlaskForm):
    lat = StringField('Latitude: ',
    validators=[DataRequired()])
    long = StringField('Longitude: ',
    validators=[DataRequired()])
    submit = SubmitField('Submit')
