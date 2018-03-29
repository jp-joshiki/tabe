from . import db
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Float, String, Text, JSON


class Restaurant(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    url = Column(String(300))
    tel = Column(String(100))
    images = Column(JSON)

    tabelog_id = Column(String(100), unique=True)
    tabelog_url = Column(String(300))
    tabelog_rate = Column(Float)

    tabelog_lunch_rate = Column(Float)
    tabelog_lunch_price_min = Column(Integer)
    tabelog_lunch_price_max = Column(Integer)
    tabelog_dinner_rate = Column(Float)
    tabelog_dinner_price_min = Column(Integer)
    tabelog_dinner_price_max = Column(Integer)

    tabelog_address = Column(Text)

    lat = Column(Float)
    lng = Column(Float)

    tags = relationship('Tag', secondary='restaurant_tag',
                        backref='restaurants', lazy='joined')
    categories = relationship('Category', secondary='restaurant_category',
                              backref='restaurants', lazy='joined')
    offdays = relationship('Offday', secondary='restaurant_offday',
                           backref='restaurants', lazy='joined')

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            address=self.tabelog_address,
            images=self.images,
            tabelog_url=self.tabelog_url,
            tabelog_rate=self.tabelog_rate,
            lat=self.lat,
            lng=self.lng,
            tags=self.tags,
        )
