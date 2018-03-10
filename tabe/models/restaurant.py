from .base import db
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Float, String, Text, JSON


class Restaurant(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    images = Column(JSON)

    tabelog_id = Column(String(100), unique=True)
    tabelog_url = Column(String(300))
    tabelog_rate = Column(Float)
    tabelog_address = Column(Text)

    lat = Column(Float)
    lng = Column(Float)

    tags = relationship('Tag', secondary='restaurant_tag')
