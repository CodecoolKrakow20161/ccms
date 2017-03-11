from flask import Blueprint, render_template, request, redirect, url_for
from app.mod_people.forms import PersonForm

# Define the blueprint: 'people', set its url prefix: app.url/people
mod_people = Blueprint('people', __name__, url_prefix='/people')

@mod_people.route('/')
def index():
    return render_template('people/index.html')

@mod_people.route('/new', methods=['GET', 'POST'])
def new():
    form = PersonForm(request.form)
    return render_template('people/new.html', form=form)