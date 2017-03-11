from flask import Blueprint, render_template, request, redirect, url_for

# Define the blueprint: 'people', set its url prefix: app.url/people
mod_people = Blueprint('people', __name__, url_prefix='/people')

@mod_people.route('/')
def index():
    return render_template('people/index.html')