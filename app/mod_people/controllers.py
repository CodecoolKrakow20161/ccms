from flask import Blueprint, render_template

# Define the blueprint: 'people', set its url prefix: app.url/people
mod_people = Blueprint('people', __name__, url_prefix='/people')

# Set the route and accepted methods
@mod_people.route('/', methods=['GET'])
def index():
    return render_template('people/index.html')