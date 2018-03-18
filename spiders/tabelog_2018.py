from ._base import BaseSpider
from tabe.models.tag import (
    TABELOG_2018,
    TABELOG_2018_GOLD,
    TABELOG_2018_SILVER,
    TABELOG_2018_BRONZE,
    TABELOG_2018_BEST_NEW_ENTRY,
    TABELOG_2018_BEST_HOSPITALITY,
    TABELOG_2018_BEST_REGIONAL,
    TABELOG_2018_BEST_CHEFS_CHOICE,
)


BASE_URL = 'https://award.tabelog.com/en/2018/restaurants'

ENTRIES = [
    ('?utf8=✓&main_prizes[]=gold&genre_id=0&prefecture_id=0',
     TABELOG_2018_GOLD),
    ('?utf8=✓&main_prizes[]=silver&genre_id=0&prefecture_id=0',
     TABELOG_2018_SILVER),
    ('?utf8=✓&main_prizes[]=bronze&genre_id=0&prefecture_id=0',
     TABELOG_2018_BRONZE),
    ('?utf8=✓&sub_prizes[]=new_entry_prize&genre_id=0&prefecture_id=0',
     TABELOG_2018_BEST_NEW_ENTRY),
    ('?utf8=✓&sub_prizes[]=hospitality_prize&genre_id=0&prefecture_id=0',
     TABELOG_2018_BEST_HOSPITALITY),
    ('?utf8=✓&sub_prizes[]=region_prize&genre_id=0&prefecture_id=0',
     TABELOG_2018_BEST_REGIONAL),
    ('?utf8=✓&sub_prizes[]=chefs_choice_prize&genre_id=0&prefecture_id=0',
     TABELOG_2018_BEST_CHEFS_CHOICE)
]


class Tabelog2018Spider(BaseSpider):
    def run(self):
        for entry in ENTRIES:
            self.parse_list(entry[0], [TABELOG_2018, entry[1]])

    def parse_list(self, path, tags):
        url = BASE_URL + path
        r = self.fetch(url).html
        items = r.find('ul.tta2018-rstlst__list', first=True)
        items = items.find('li.tta2018-rstlst__item')
        for item in items:
            self.parse_item(item, tags)

    def parse_item(self, item, tags):
        a = item.find('a.tta2018-rstlst__target', first=True)
        url = a.attrs['href']
        url = url.replace('/en', '')
        if not url:
            return
        self.parse_tabelog(url, tags)
