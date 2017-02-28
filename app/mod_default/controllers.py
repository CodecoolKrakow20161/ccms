from flask import Blueprint, render_template

# Define the blueprint: 'people', set its url prefix: app.url/people
mod_default = Blueprint('default', __name__)

# Set the route and accepted methods
@mod_default.route('/', methods=['GET'])
def index():
    return render_template('default/index.html')