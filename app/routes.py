from app import app
from flask import render_template, url_for, redirect
from app.forms import FeatureLayerForm


@app.route('/')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = FeatureLayerForm()

    # when form is submitted, redirect to scene page, and pass hosted feature layer id to change extent of map
    if form.validate_on_submit():
        # return "The portalitem id is: {}".format(form.id.data)
        return redirect(url_for('scene', id=form.id.data))

    return render_template('index.html', title='Home', form=form)

@app.route('/scene')
@app.route('/scene/<id>')
def scene(id=''):
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('scene.html', title='Scene', id=id)
