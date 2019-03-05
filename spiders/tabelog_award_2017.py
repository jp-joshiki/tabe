from tabe.consts import (
    TABELOG_AWARD_2017_GOLD,
    TABELOG_AWARD_2017_SILVER,
    TABELOG_AWARD_2017_BRONZE
)
from ._base import BaseSpider

BASE_URL = 'https://award.tabelog.com/2017/rstlist'

ENTRIES = [
    (['utf8=✓&gold=true&genre_id=0&prefecture_id=0'], TABELOG_AWARD_2017_GOLD),
    ([f'genre_id=0&page={x}&prefecture_id=0&silver=true' for x in range(1, 3)], TABELOG_AWARD_2017_SILVER),
    ([f'bronze=true&genre_id=0&page={x}&prefecture_id=0' for x in range(1, 9)], TABELOG_AWARD_2017_BRONZE),
]


class TabelogAward2017Spider(BaseSpider):
    target = './data/tabelog_award_2017.json'

    def run(self):
        for entry in ENTRIES:
            for param in entry[0]:
                self.parse_list(param, entry[1])
        self.store()

    def parse_list(self, path, tag):
        url = BASE_URL + '?' + path
        r = self.fetch(url).html
        items = r.find('ul.award2017-rstlst__items', first=True)
        items = items.find('li.award2017-rstlst__item')
        for item in items:
            self.parse_item(item, tag)

    def parse_item(self, item, tag):
        a = item.find('a.award2017-rstlst__target', first=True)
        url = a.attrs['href']
        self.add(url, tag)
