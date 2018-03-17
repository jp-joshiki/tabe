from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String

from .base import db


class RestaurantTag(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name_ja = Column(String(100))

    @staticmethod
    def update():
        for group in _GROUPED:
            group_name = group['name_ja']
            group_tag = Tag.query.get(group['id'])
            if not group_tag:
                group_tag = Tag(id=group['id'])
            group_tag.name_ja = group_name
            with db.auto_commit():
                db.session.add(group_tag)
            for item in group['items']:
                tag = Tag.query.get(item['id'])
                if not tag:
                    item = Tag(id=item['id'])
                tag.name_ja = group_name + ' ' + item['name_ja']
                with db.auto_commit():
                    db.session.add(tag)

    def to_dict(self):
        return dict(
            id=self.id,
            name_ja=self.name_ja,
        )

    @staticmethod
    def grouped():
        return _GROUPED


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

_GROUPED = [{
    'id': TABELOG_2017,
    'name_ja': '食べログ 百名店 2017',
    'items': [
        {
            'id': TABELOG_2017_HAMBURGER,
            'name_ja': 'ハンバーガー',
        },
        {
            'id': TABELOG_2017_PIZZA,
            'name_ja': 'ピザ',
        },
        {
            'id': TABELOG_2017_PORK_CUTLET,
            'name_ja': 'とんかつ',
        },
        {
            'id': TABELOG_2017_CURRY,
            'name_ja': 'カレー',
        },
        {
            'id': TABELOG_2017_SOBA,
            'name_ja': 'そば',
        },
        {
            'id': TABELOG_2017_UDON,
            'name_ja': 'うどん',
        },
        {
            'id': TABELOG_2017_RAMEN_TOKYO,
            'name_ja': 'TOKYO ラーメン'
        },
        {
            'id': TABELOG_2017_RAMEN_EASE,
            'name_ja': 'EAST ラーメン'
        },
        {
            'id': TABELOG_2017_RAMEN_WEST,
            'name_ja': 'WEST ラーメン'
        },
        {
            'id': TABELOG_2017_SWEETS,
            'name_ja': 'スイーツ',
        },
        {
            'id': TABELOG_2017_PAN,
            'name_ja': 'パン',
        },
    ]
}]
