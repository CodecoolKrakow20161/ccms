from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.__version__ import version

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Add app_version variable to Jinja2 templates context
@app.context_processor
def app_version():
    return dict(app_version=version)

from app.mod_default.controllers import mod_default
from app.mod_classes.controllers import mod_classes

app.register_blueprint(mod_default)
app.register_blueprint(mod_classes)
