from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.mod_people.forms import PersonForm
from app.mod_people.models import Person

mod_people = Blueprint('people', __name__, url_prefix='/people')

@mod_people.route('/')
def index():
    return render_template('people/index.html')

@mod_people.route('/new', methods=['GET', 'POST'])
def new():
    form = PersonForm(request.form)
    if request.method == "POST" and form.validate():
        person = Person(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                        phone=form.phone.data)

        db.session.add(person)
        db.session.commit()

        return render_template("people/index.html")

    return render_template('people/new.html', form=form)