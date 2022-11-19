import logging
import os
from flask import Flask
from flask_cors import CORS
from app import main
from app.main.api import api
from app.main.database import db, migration
from app.main.log_config import LOGGING_CONFIG

# Flask App Initialization
app = Flask(__name__)
CORS(app)
app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'default')])

# Logs Initialization
console = logging.getLogger('console')

# Database ORM Initialization
from app import models
# import app.main.main

db.init_app(app)

# Database Migrations Initialization
migration.init_app(app, db)

# Flask API Initialization
api.init_app(app)

#
