from . import db
from .tag import SUMMARY_TAGS
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Float, String, Text


class Restaurant(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    url = Column(String(300))
    tel = Column(String(100))
    images = Column(String)

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
                        backref='restaurants')
    categories = relationship('Category', secondary='restaurant_category',
                              backref='restaurants')
    offdays = relationship('Offday', secondary='restaurant_offday',
                           backref='restaurants')

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            url=self.url,
            tel=self.tel,
            address=self.tabelog_address,
            images=self.images,
            tabelog_url=self.tabelog_url,
            tabelog_rate=self.tabelog_rate,
            tabelog_lunch_rate=self.tabelog_lunch_rate,
            tabelog_lunch_price_min=self.tabelog_lunch_price_min,
            tabelog_lunch_price_max=self.tabelog_lunch_price_max,
            tabelog_dinner_rate=self.tabelog_dinner_rate,
            tabelog_dinner_price_min=self.tabelog_dinner_price_min,
            tabelog_dinner_price_max=self.tabelog_dinner_price_max,
            lat=self.lat,
            lng=self.lng,

            categories=self.categories if self.categories else None,
            offdays=self.offdays if self.offdays else None,
            tags=[x for x in self.tags if x.id not in SUMMARY_TAGS],
        )
