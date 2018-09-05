from pathlib import Path

_here = Path(__file__).resolve()
_SQLALCHEMY_DATABASE_URI = _here.parent.parent / 'store.db'

DEBUG = True
SQLALCHEMY_DATABASE_URI = f'sqlite:///{_SQLALCHEMY_DATABASE_URI}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
