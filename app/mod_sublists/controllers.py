from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.mod_sublists.models import Sublist
from app.mod_sublists.forms import SublistForm

mod_sublists = Blueprint('sublists', __name__, url_prefix='/sublists')

@mod_sublists.route('/')
def index():
    sublists = Sublist.query.all()
    return render_template('sublists/index.html', sublists=sublists)

@mod_sublists.route('/new', methods=['GET', 'POST'])
def new():
    form = SublistForm(request.form)
    if request.method == "POST" and form.validate():
        sublist = Sublist(name=form.name.data, description=form.description.data)
        db.session.add(sublist)
        db.session.commit()
        return redirect(url_for('sublists.index'))

    return render_template('sublists/new.html', form=form)

@mod_sublists.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    sublist = Sublist.query.get_or_404(id)
    db.session.delete(sublist)
    db.session.commit()
    return redirect(url_for('sublists.index'))