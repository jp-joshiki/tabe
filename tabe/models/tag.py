from ._utils import I18n


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

SUMMARY_TAGS = [
    TABELOG_2017_TOP_100,
    TABELOG_2018,
    MICHELIN_2018,
]

_GROUPED_TAGS = [
    {
        'id': MICHELIN_2018,
        'name': I18n.complex(ja='ミシュラン 2018',
                             en='Michelin 2018',
                             cn='米其林2018'),
        'items': [
            {
                'id': MICHELIN_2018_3STAR,
                'name': I18n.complex(ja='三つ星',
                                     en='3 star',
                                     cn='三星'),
            },
            {
                'id': MICHELIN_2018_2STAR,
                'name': I18n.complex(ja='二つ星',
                                     en='2 star',
                                     cn='二星'),
            },
            {
                'id': MICHELIN_2018_1STAR,
                'name': I18n.complex(ja='一つ星',
                                     en='1 star',
                                     cn='一星'),
            },
            {
                'id': MICHELIN_2018_BIG_GOURMAND,
                'name': I18n.complex(ja='ビブグルマン',
                                     en='Bib Gourmand',
                                     cn='超值套餐'),
            },
        ],
    },
    {
        'id': TABELOG_2018,
        'name': I18n.simple('Tabelog Award 2018'),
        'items': [
            {
                'id': TABELOG_2018_GOLD,
                'name': I18n.simple('Gold'),
            },
            {
                'id': TABELOG_2018_SILVER,
                'name': I18n.simple('Silver'),
            },
            {
                'id': TABELOG_2018_BRONZE,
                'name': I18n.simple('Bronze'),
            },
            {
                'id': TABELOG_2018_BEST_NEW_ENTRY,
                'name': I18n.simple('Best New Entry'),
            },
            {
                'id': TABELOG_2018_BEST_HOSPITALITY,
                'name': I18n.simple('Best Hospitality'),
            },
            {
                'id': TABELOG_2018_BEST_REGIONAL,
                'name': I18n.simple('Best Regional Restaurant'),
            },
            {
                'id': TABELOG_2018_BEST_CHEFS_CHOICE,
                'name': I18n.simple("Best Chef's choice"),
            }
        ],
    },
    {
        'id': TABELOG_2017_TOP_100,
        'name': I18n.complex(ja='食べログ 百名店 2017',
                             en='Tabelog Top100 2017',
                             cn='Tabelog 百名店 2017', ),
        'items': [
            {
                'id': TABELOG_2017_TOP_100_HAMBURGER,
                'name': I18n.complex(
                    ja='ハンバーガー', en='Hamburger', cn='漢堡'
                ),
            },
            {
                'id': TABELOG_2017_TOP_100_PIZZA,
                'name': I18n.complex(
                    ja='ピザ', en='Pizza', cn='披薩',
                ),
            },
            {
                'id': TABELOG_2017_TOP_100_PORK_CUTLET,
                'name': I18n.complex(
                    ja='とんかつ', en='Pork Cutlet', cn='炸豬排'
                ),
            },
            {
                'id': TABELOG_2017_TOP_100_CURRY,
                'name': I18n.complex(
                    ja='カレー', en='Curry', cn='咖喱'
                ),
            },
            {
                'id': TABELOG_2017_TOP_100_SOBA,
                'name': I18n.complex(
                    ja='そば', en='Soba', cn='蕎麥麵'
                ),
            },
            {
                'id': TABELOG_2017_TOP_100_UDON,
                'name': I18n.complex(
                    ja='うどん', en='Udon', cn='烏冬面'
                ),
            },
            {
                'id': TABELOG_2017_TOP_100_RAMEN_TOKYO,
                'name': I18n.complex(
                    ja='Tokyo ラーメン', en='Tokyo Ramen', cn='東京拉麵'
                )
            },
            {
                'id': TABELOG_2017_TOP_100_RAMEN_EASE,
                'name': I18n.complex(
                    ja='East ラーメン', en='East Ramen', cn='關東拉麵'
                )
            },
            {
                'id': TABELOG_2017_TOP_100_RAMEN_WEST,
                'name': I18n.complex(
                    ja='WEST ラーメン', en='West Ramen', cn='關西拉麵'
                )
            },
            {
                'id': TABELOG_2017_TOP_100_SWEETS,
                'name': I18n.complex(
                    ja='スイーツ', en='Sweets', cn='甜品'
                ),
            },
            {
                'id': TABELOG_2017_TOP_100_PAN,
                'name': I18n.complex(
                    ja='パン', en='Pan', cn='麵包'
                ),
            },
        ]
    },
]
