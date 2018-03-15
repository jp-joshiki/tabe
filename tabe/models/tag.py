from .base import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String


class RestaurantTag(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name_ja = Column(String(100))

    @staticmethod
    def update():
        for id_, detail in _tags.items():
            tag = Tag.query.get(id_)
            if not tag:
                tag = Tag(id=id_, name_ja=detail[0])
            with db.auto_commit():
                db.session.add(tag)

    def to_dict(self):
        return dict(
            id=self.id,
            name_ja=self.name_ja,
        )


TABELOG_2017 = 1
TABELOG_2017_HAMBURGER = 2
TABELOG_2017_PIZZA = 3
TABELOG_2017_PORK_CUTLET = 4
TABELOG_2017_CURRY = 5
TABELOG_2017_SOBA = 6
TABELOG_2017_UDON = 7
TABELOG_2017_RAMEN_TOKYO = 8
TABELOG_2017_RAMEN_EASE = 9
TABELOG_2017_RAMEN_WEST = 10
TABELOG_2017_SWEETS = 11
TABELOG_2017_PAN = 12

_tags = {
    TABELOG_2017: ['食べログ 百名店 2017'],
    TABELOG_2017_HAMBURGER: ['食べログ ハンバーガー 百名店 2017'],
    TABELOG_2017_PIZZA: ['食べログ ピザ 百名店 2017'],
    TABELOG_2017_PORK_CUTLET: ['食べログ とんかつ 百名店 2017'],
    TABELOG_2017_CURRY: ['食べログ カレー 百名店 2017'],
    TABELOG_2017_SOBA: ['食べログ そば 百名店 2017'],
    TABELOG_2017_UDON: ['食べログ うどん 百名店 2017'],
    TABELOG_2017_RAMEN_TOKYO: ['食べログ ラーメン 百名店 TOKYO 2017'],
    TABELOG_2017_RAMEN_EASE: ['食べログ ラーメン 百名店 EAST 2017'],
    TABELOG_2017_RAMEN_WEST: ['食べログ ラーメン 百名店 WEST 2017'],
    TABELOG_2017_SWEETS: ['食べログ スイーツ 百名店 2017'],
    TABELOG_2017_PAN: ['食べログ パン 百名店 2017'],
}
