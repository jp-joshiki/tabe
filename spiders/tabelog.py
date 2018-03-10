import re

from ._base import BaseSpider
from tabe.models.tag import (
    TABELOG_2017,
    TABELOG_2017_HAMBURGER,
    TABELOG_2017_PIZZA,
    TABELOG_2017_PORK_CUTLET,
    TABELOG_2017_CURRY,
    TABELOG_2017_SOBA,
    TABELOG_2017_UDON,
    TABELOG_2017_RAMEN_TOKYO,
    TABELOG_2017_RAMEN_EASE,
    TABELOG_2017_RAMEN_WEST,
    TABELOG_2017_SWEETS,
    TABELOG_2017_PAN,
)


BASE_URL = 'https://award.tabelog.com/hyakumeiten/2017'


ENTRIES = [
    ('hamburger/japan', TABELOG_2017_HAMBURGER),
    ('pizza/japan', TABELOG_2017_PIZZA),
    ('tonkatsu/japan', TABELOG_2017_PORK_CUTLET),
    ('curry/japan', TABELOG_2017_CURRY),
    ('soba/japan', TABELOG_2017_SOBA),
    ('udon/japan', TABELOG_2017_UDON),
    ('ramen/tokyo', TABELOG_2017_RAMEN_TOKYO),
    ('ramen/east', TABELOG_2017_RAMEN_EASE),
    ('ramen/west', TABELOG_2017_RAMEN_WEST),
    ('sweets/japan', TABELOG_2017_SWEETS),
    ('pan/japan', TABELOG_2017_PAN)
]


class TabelogSpider(BaseSpider):
    def run(self):
        for entry in ENTRIES:
            self.parse_list(entry[0], [TABELOG_2017, entry[1]])

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
        id_ = url.split('/')[-2]

        r = self.fetch(url).html
        name = r.find('h2.display-name', first=True).text.strip()
        rate = r.find('span.rdheader-rating__score-val-dtl', first=True)
        rate = float(rate.text.strip())
        address = r.find('p.rstinfo-table__address', first=True).text.strip()
        images = r.find('p.rstdtl-top-postphoto__photo')
        images = [x.find('a', first=True).attrs['href'] for x in images]
        location = r.find('p.rstinfo-actions__btn',
                          containing='印刷ページを表示',
                          first=True) \
            .find('a', first=True).attrs['data-print-url']
        location = re.search('lat=(.*)&lng=(.*)&rcd', location)
        lat = float(location.group(1))
        lng = float(location.group(2))

        data = dict(
            name=name,
            tabelog_id=id_,
            tabelog_url=url,
            tabelog_rate=rate,
            tabelog_address=address,
            images=images,
            lat=lat,
            lng=lng,
        )
        self.store(tags, **data)
