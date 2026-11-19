"""
Account Service Application Initialization
"""

from flask import Flask
from flask_talisman import Talisman

# Initialize Flask application
app = Flask(__name__)

# Enable security headers using Flask-Talisman
Talisman(app)

# Keep the rest of your existing application
# configuration, database setup, and imports below.
