from flask import Flask, render_template

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_people.controllers import mod_people

app.register_blueprint(mod_people)