from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FeatureLayerForm(FlaskForm):
    id = StringField(label='', validators=[DataRequired()], render_kw={"placeholder": "Hosted Feature Layer"})
    submit_url = SubmitField('Submit')
