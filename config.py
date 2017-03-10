# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and
# will be disabled by default in the future
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, 'app.db'))
DATABASE_CONNECT_OPTIONS = {}

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = os.getenv("CSRF_SECRET_KEY", "secret")

# Secret key for signing cookies
SECRET_KEY = os.getenv("SECRET_KEY", "secret")