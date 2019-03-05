from ._base import BaseSpider
from tabe.consts import (
    TABELOG_2018_TOP_100_YANKINIKU,
    TABELOG_2018_TOP_100_PIZZA,
    TABELOG_2018_TOP_100_OKONOMIYAKI,
    TABELOG_2018_TOP_100_TONKATSU,
    TABELOG_2018_TOP_100_CURRY,
    TABELOG_2018_TOP_100_HAMBURGER,
    TABELOG_2018_TOP_100_YAKITORI,
    TABELOG_2018_TOP_100_UNAGI,
    TABELOG_2018_TOP_100_UDON,
    TABELOG_2018_TOP_100_SOBA,
    TABELOG_2018_TOP_100_TOKYO_RAMEN,
    TABELOG_2018_TOP_100_EAST_RAMEN,
    TABELOG_2018_TOP_100_WEST_RAMEN,
    TABELOG_2018_TOP_100_PAN,
    TABELOG_2018_TOP_100_TOKYO_SWEETS,
    TABELOG_2018_TOP_100_EAST_SWEETS,
    TABELOG_2018_TOP_100_WEST_SWEETS,
)

BASE_URL = 'https://award.tabelog.com/hyakumeiten/2018/'

ENTRIES = [
    ('yakiniku/japan', TABELOG_2018_TOP_100_YANKINIKU),
    ('pizza/japan', TABELOG_2018_TOP_100_PIZZA),
    ('okonomiyaki/japan', TABELOG_2018_TOP_100_OKONOMIYAKI),
    ('tonkatsu/japan', TABELOG_2018_TOP_100_TONKATSU),
    ('curry/japan', TABELOG_2018_TOP_100_CURRY),
    ('hamburger/japan', TABELOG_2018_TOP_100_HAMBURGER),
    ('yakitori/japan', TABELOG_2018_TOP_100_YAKITORI),
    ('unagi/japan', TABELOG_2018_TOP_100_UNAGI),
    ('udon/japan', TABELOG_2018_TOP_100_UDON),
    ('soba/japan', TABELOG_2018_TOP_100_SOBA),
    ('ramen/tokyo', TABELOG_2018_TOP_100_TOKYO_RAMEN),
    ('ramen/east', TABELOG_2018_TOP_100_EAST_RAMEN),
    ('ramen/west', TABELOG_2018_TOP_100_WEST_RAMEN),
    ('pan/japan', TABELOG_2018_TOP_100_PAN),
    ('sweets/tokyo', TABELOG_2018_TOP_100_TOKYO_SWEETS),
    ('sweets/east', TABELOG_2018_TOP_100_EAST_SWEETS),
    ('sweets/west', TABELOG_2018_TOP_100_WEST_SWEETS),
]


class Tabelog100Top2018Spider(BaseSpider):
    target = './data/tabelog_100_top_2018.json'

    def run(self):
        for (path, tag) in ENTRIES:
            url = f'{BASE_URL}/{path}'
            r = self.fetch(url).html
            items = r.find('li.hyakumeiten-rstlist__item')
            for item in items:
                a = item.find('a.hyakumeiten-rstlist__target', first=True)
                target = a.attrs['href'].split('?')[0]
                self.add(target, tag)
        self.store()
