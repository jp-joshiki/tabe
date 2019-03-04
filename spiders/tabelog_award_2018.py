import json

from tabe.models.tag import (
    TABELOG_2018_GOLD,
    TABELOG_2018_SILVER,
    TABELOG_2018_BRONZE,
    TABELOG_2018_BEST_NEW_ENTRY,
    TABELOG_2018_BEST_HOSPITALITY,
    TABELOG_2018_BEST_REGIONAL,
    TABELOG_2018_BEST_CHEFS_CHOICE,
)
from ._base import BaseSpider

BASE_URL = 'https://award.tabelog.com/2018/restaurants'

ENTRIES = [
    (['?utf8=✓&main_prizes%5B%5D=gold&genre_id=0&prefecture_id=0'],
     TABELOG_2018_GOLD),
    ([
         '?utf8=✓&main_prizes%5B%5D=silver&genre_id=0&prefecture_id=0',
         '?genre_id=0&main_prizes%5B%5D=silver&page=2&prefecture_id=0',
     ],
     TABELOG_2018_SILVER),
    ([
         '?utf8=✓&main_prizes%5B%5D=bronze&genre_id=0&prefecture_id=0',
         '?genre_id=0&main_prizes%5B%5D=bronze&page=2&prefecture_id=0',
         '?genre_id=0&main_prizes%5B%5D=bronze&page=3&prefecture_id=0',
         '?genre_id=0&main_prizes%5B%5D=bronze&page=4&prefecture_id=0',
         '?genre_id=0&main_prizes%5B%5D=bronze&page=5&prefecture_id=0',
     ],
     TABELOG_2018_BRONZE),
    (['?utf8=✓&sub_prizes[]=new_entry_prize&genre_id=0&prefecture_id=0'],
     TABELOG_2018_BEST_NEW_ENTRY),
    (['?utf8=✓&sub_prizes[]=hospitality_prize&genre_id=0&prefecture_id=0'],
     TABELOG_2018_BEST_HOSPITALITY),
    (['?utf8=✓&sub_prizes[]=region_prize&genre_id=0&prefecture_id=0'],
     TABELOG_2018_BEST_REGIONAL),
    (['?utf8=✓&sub_prizes[]=chefs_choice_prize&genre_id=0&prefecture_id=0'],
     TABELOG_2018_BEST_CHEFS_CHOICE)
]


class TabelogAward2018Spider(BaseSpider):
    data = {}

    def run(self):
        for entry in ENTRIES:
            for param in entry[0]:
                self.parse_list(param, entry[1])
        with open('./data/tabelog_award_2018.json', 'w') as f:
            data = list(self.data.values())
            data = sorted(data, key=lambda x: x['tabelog_url'])
            json.dump(data, f, indent=4)

    def parse_list(self, path, tag):
        url = BASE_URL + path
        r = self.fetch(url).html
        items = r.find('ul.tta2018-rstlst__list', first=True)
        items = items.find('li.tta2018-rstlst__item')
        for item in items:
            self.parse_item(item, tag)

    def parse_item(self, item, tag):
        a = item.find('a.tta2018-rstlst__target', first=True)
        url = a.attrs['href']
        prev = self.data.get(url)
        if prev:
            prev['tags'] = prev['tags'] + [tag]
            self.data[url] = prev
        else:
            self.data[url] = dict(tabelog_url=url, tags=[tag])
        print(self.data[url])
