from . import db
from sqlalchemy import Column
from sqlalchemy import Integer, Text, String


class Restaurant(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    tabelog_url = Column(String(300), unique=True, nullable=False)

    tags = Column(Text)
