import os

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from .models import db


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'to_dict'):
            return o.to_dict()
        return _JSONEncoder.default(self, o)


class Flask(_Flask):
    json_encoder = JSONEncoder


def _inject_config(app):
    base_settings = os.path.join(app.root_path, '../conf/base_settings.py')
    app.config.from_pyfile(base_settings)

    is_prod = os.environ.get('IS_HEROKU', None)
    if is_prod:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    else:
        local_settings = os.path.join(app.root_path, '../local_settings.py')
        app.config.from_pyfile(local_settings)


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
