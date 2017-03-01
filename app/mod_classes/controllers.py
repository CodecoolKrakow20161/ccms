from flask import Blueprint, render_template, request, redirect
from app import db
from app.mod_classes.models import Klass
from app.mod_classes.forms import KlassForm

# Define the blueprint: 'people', set its url prefix: app.url/people
mod_classes = Blueprint('classes', __name__, url_prefix='/classes')

# Set the route and accepted methods
@mod_classes.route('/', methods=['GET'])
def index():
    klasses = Klass.query.all()
    return render_template('classes/index.html', klasses=klasses)

@mod_classes.route('/new', methods=['GET', 'POST'])
def new():
    form = KlassForm(request.form)
    if form.validate_on_submit():
        klass = Klass()
        form.populate_obj(klass)

        db.session.add(klass)
        db.session.commit()

        return redirect('/classes')


    return render_template('classes/new.html', form=form)