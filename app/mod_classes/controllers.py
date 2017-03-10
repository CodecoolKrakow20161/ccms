from flask import Blueprint, render_template, request, redirect, url_for
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
    if request.method == "POST" and form.validate():
        klass = Klass(name=form.name.data)

        db.session.add(klass)
        db.session.commit()

        return redirect(url_for('classes.index'))

    return render_template('classes/new.html', form=form)


@mod_classes.route('/edit/<int:class_id>', methods=['GET', 'POST'])
def edit(class_id):
    klass = Klass.query.get(class_id)
    form = KlassForm(formdata=request.form, obj=klass)
    if request.method == "POST" and form.validate():
        klass.name = form.name.data
        db.session.commit()

        return redirect(url_for('classes.index'))

    return render_template('classes/edit.html', form=form, klass=klass)


@mod_classes.route('/delete/<int:class_id>', methods=['GET'])
def delete(class_id):
    klass = Klass.query.get(class_id)

    db.session.delete(klass)
    db.session.commit()

    return redirect(url_for('classes.index'))
