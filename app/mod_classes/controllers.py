from flask import Blueprint, render_template

# Define the blueprint: 'people', set its url prefix: app.url/people
mod_classes = Blueprint('classes', __name__, url_prefix='/classes')

# Set the route and accepted methods
@mod_classes.route('/', methods=['GET'])
def index():
    return render_template('classes/index.html')