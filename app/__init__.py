from flask import Flask, render_template

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_default.controllers import mod_default

app.register_blueprint(mod_default)