from ._base import BaseSpider
from tabe.models.tag import (
    TABELOG_2017_TOP_100,
    TABELOG_2017_TOP_100_HAMBURGER,
    TABELOG_2017_TOP_100_PIZZA,
    TABELOG_2017_TOP_100_PORK_CUTLET,
    TABELOG_2017_TOP_100_CURRY,
    TABELOG_2017_TOP_100_SOBA,
    TABELOG_2017_TOP_100_UDON,
    TABELOG_2017_TOP_100_RAMEN_TOKYO,
    TABELOG_2017_TOP_100_RAMEN_EASE,
    TABELOG_2017_TOP_100_RAMEN_WEST,
    TABELOG_2017_TOP_100_SWEETS,
    TABELOG_2017_TOP_100_PAN,
)


BASE_URL = 'https://award.tabelog.com/hyakumeiten/2017'


ENTRIES = [
    ('hamburger/japan', TABELOG_2017_TOP_100_HAMBURGER),
    ('pizza/japan', TABELOG_2017_TOP_100_PIZZA),
    ('tonkatsu/japan', TABELOG_2017_TOP_100_PORK_CUTLET),
    ('curry/japan', TABELOG_2017_TOP_100_CURRY),
    ('soba/japan', TABELOG_2017_TOP_100_SOBA),
    ('udon/japan', TABELOG_2017_TOP_100_UDON),
    ('ramen/tokyo', TABELOG_2017_TOP_100_RAMEN_TOKYO),
    ('ramen/east', TABELOG_2017_TOP_100_RAMEN_EASE),
    ('ramen/west', TABELOG_2017_TOP_100_RAMEN_WEST),
    ('sweets/japan', TABELOG_2017_TOP_100_SWEETS),
    ('pan/japan', TABELOG_2017_TOP_100_PAN)
]


class Tabelog2017Top100Spider(BaseSpider):
    def run(self):
        for entry in ENTRIES:
            self.parse_list(entry[0], [TABELOG_2017_TOP_100, entry[1]])

    def parse_list(self, path, tags):
        url = BASE_URL + '/' + path
        r = self.fetch(url)
        items = r.html.find('ul.rstlist', first=True)
        items = items.find('li.rstlist__item')
        for item in items:
            self.parse_item(item, tags)

    def parse_item(self, item, tags):
        a = item.find('a.rstlist__target', first=True)
        url = a.attrs['href']
        url = url.split('?')[0]
        self.parse_tabelog(url, tags)
