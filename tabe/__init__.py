import os

from flask import Flask
from .models import db


def _inject_config(app):
    base_settings = os.path.join(app.root_path, '../conf/base_settings.py')
    app.config.from_pyfile(base_settings)


def create_basic_app():
    app = Flask(__name__)
    _inject_config(app)
    db.init_app(app)
    return app


def create_app():
    app = Flask(__name__)
    _inject_config(app)
    db.init_app(app)
    return app
