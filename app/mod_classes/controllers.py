from flask import Blueprint, render_template
from app import db
from app.mod_classes.models import Klass

# Define the blueprint: 'people', set its url prefix: app.url/people
mod_classes = Blueprint('classes', __name__, url_prefix='/classes')

# Set the route and accepted methods
@mod_classes.route('/', methods=['GET'])
def index():
    klasses = Klass.query.all()
    return render_template('classes/index.html', klasses=klasses)

@mod_classes.route('/new', methods=['GET'])
def new():
    return render_template('classes/new.html')