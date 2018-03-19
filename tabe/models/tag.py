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
                    tag = Tag(id=item['id'])
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


TABELOG_2017_TOP_100 = 1
TABELOG_2017_TOP_100_HAMBURGER = 2
TABELOG_2017_TOP_100_PIZZA = 3
TABELOG_2017_TOP_100_PORK_CUTLET = 4
TABELOG_2017_TOP_100_CURRY = 5
TABELOG_2017_TOP_100_SOBA = 6
TABELOG_2017_TOP_100_UDON = 7
TABELOG_2017_TOP_100_RAMEN_TOKYO = 8
TABELOG_2017_TOP_100_RAMEN_EASE = 9
TABELOG_2017_TOP_100_RAMEN_WEST = 10
TABELOG_2017_TOP_100_SWEETS = 11
TABELOG_2017_TOP_100_PAN = 12

TABELOG_2018 = 13
TABELOG_2018_GOLD = 14
TABELOG_2018_SILVER = 15
TABELOG_2018_BRONZE = 16
TABELOG_2018_BEST_NEW_ENTRY = 17
TABELOG_2018_BEST_HOSPITALITY = 18
TABELOG_2018_BEST_REGIONAL = 19
TABELOG_2018_BEST_CHEFS_CHOICE = 20

MICHELIN_2018 = 21
MICHELIN_2018_1STAR = 22
MICHELIN_2018_2STAR = 23
MICHELIN_2018_3STAR = 24
MICHELIN_2018_BIG_GOURMAND = 25

_GROUPED = [
    # {
    #     'id': MICHELIN_2018,
    #     'name_ja': 'ミシュラン 2018',
    #     'items': [
    #         {
    #             'id': MICHELIN_2018_BIG_GOURMAND,
    #             'name_ja': 'ビブグルマン',
    #         },
    #         {
    #             'id': MICHELIN_2018_1STAR,
    #             'name_ja': '一つ星',
    #         },
    #         {
    #             'id': MICHELIN_2018_2STAR,
    #             'name_ja': '二つ星',
    #         },
    #         {
    #             'id': MICHELIN_2018_3STAR,
    #             'name_ja': '三つ星',
    #         },
    #     ],
    # },
    {
        'id': TABELOG_2018,
        'name_ja': 'Tabelog Award 2018',
        'items': [
            {
                'id': TABELOG_2018_GOLD,
                'name_ja': 'Gold',
            },
            {
                'id': TABELOG_2018_SILVER,
                'name_ja': 'Silver',
            },
            {
                'id': TABELOG_2018_BRONZE,
                'name_ja': 'Bronze',
            },
            {
                'id': TABELOG_2018_BEST_NEW_ENTRY,
                'name_ja': 'Best New Entry',
            },
            {
                'id': TABELOG_2018_BEST_HOSPITALITY,
                'name_ja': 'Best Hospitality',
            },
            {
                'id': TABELOG_2018_BEST_REGIONAL,
                'name_ja': 'Best Regional Restaurant',
            },
            {
                'id': TABELOG_2018_BEST_CHEFS_CHOICE,
                'name_ja': "Best Chef's choice",
            }
        ],
    },
    {
        'id': TABELOG_2017_TOP_100,
        'name_ja': '食べログ 百名店 2017',
        'items': [
            {
                'id': TABELOG_2017_TOP_100_HAMBURGER,
                'name_ja': 'ハンバーガー',
            },
            {
                'id': TABELOG_2017_TOP_100_PIZZA,
                'name_ja': 'ピザ',
            },
            {
                'id': TABELOG_2017_TOP_100_PORK_CUTLET,
                'name_ja': 'とんかつ',
            },
            {
                'id': TABELOG_2017_TOP_100_CURRY,
                'name_ja': 'カレー',
            },
            {
                'id': TABELOG_2017_TOP_100_SOBA,
                'name_ja': 'そば',
            },
            {
                'id': TABELOG_2017_TOP_100_UDON,
                'name_ja': 'うどん',
            },
            {
                'id': TABELOG_2017_TOP_100_RAMEN_TOKYO,
                'name_ja': 'TOKYO ラーメン'
            },
            {
                'id': TABELOG_2017_TOP_100_RAMEN_EASE,
                'name_ja': 'EAST ラーメン'
            },
            {
                'id': TABELOG_2017_TOP_100_RAMEN_WEST,
                'name_ja': 'WEST ラーメン'
            },
            {
                'id': TABELOG_2017_TOP_100_SWEETS,
                'name_ja': 'スイーツ',
            },
            {
                'id': TABELOG_2017_TOP_100_PAN,
                'name_ja': 'パン',
            },
        ]
    },
]
