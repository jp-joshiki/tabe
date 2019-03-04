from sqlalchemy import Column
from sqlalchemy import String, Float, Integer, Text

from . import db


class TabelogRestaurant(db.Model):
    id = Column(Integer, primary_key=True)
    source_url = Column(String(300), nullable=False)

    url = Column(String(300))
    rate = Column(Float)
    address = Column(Text)
    tel = Column(String(100))
    images = Column(String)

    lunch_rate = Column(Float)
    dinner_rate = Column(Float)

    lunch_price_min = Column(Integer)
    lunch_price_max = Column(Integer)
    dinner_price_min = Column(Integer)
    dinner_price_max = Column(Integer)

    lat = Column(Float)
    lng = Column(Float)
