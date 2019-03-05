from tabe.consts import (
    TABELOG_AWARD_2019_GOLD,
    TABELOG_AWARD_2019_SILVER,
    TABELOG_AWARD_2019_BRONZE,
    TABELOG_AWARD_2019_BEST_NEW_ENTRY,
    TABELOG_AWARD_2019_BEST_HOSPITALITY,
    TABELOG_AWARD_2019_BEST_REGIONAL,
    TABELOG_AWARD_2019_BEST_SOMMELIER,
    TABELOG_AWARD_2019_CHEFS_CHOICE,
)
from ._base import BaseSpider

BASE_URL = 'https://award.tabelog.com/restaurants/'

ENTRIES = [
    (['gold?utf8=✓&prize_type=gold&genre_id=0&prefecture_id=0'],
     TABELOG_AWARD_2019_GOLD),
    ([
         f'silver?genre_id=0&page={x}&prefecture_id=0' for x in range(1, 3)
     ],
     TABELOG_AWARD_2019_SILVER),
    ([
         f'bronze?genre_id=0&page={x}&prefecture_id=0' for x in range(1, 6)
     ],
     TABELOG_AWARD_2019_BRONZE),
    (['new?utf8=✓&prize_type=new&genre_id=0&prefecture_id=0'],
     TABELOG_AWARD_2019_BEST_NEW_ENTRY),
    (['hospitality?utf8=✓&prize_type=hospitality&genre_id=0&prefecture_id=0'],
     TABELOG_AWARD_2019_BEST_HOSPITALITY),
    (['regional?utf8=✓&prize_type=regional&genre_id=0&prefecture_id=0'],
     TABELOG_AWARD_2019_BEST_REGIONAL),
    (['sommelier?utf8=✓&prize_type=sommelier&genre_id=0&prefecture_id=0'],
     TABELOG_AWARD_2019_BEST_SOMMELIER),
    (['chef?utf8=✓&prize_type=chef&genre_id=0&prefecture_id=0'],
     TABELOG_AWARD_2019_CHEFS_CHOICE),
]


class TabelogAward2019Spider(BaseSpider):
    data = {}
    target = './data/tabelog_award_2019.json'

    def run(self):
        for entry in ENTRIES:
            for param in entry[0]:
                self.parse_list(param, entry[1])
        self.store()

    def parse_list(self, path, tag):
        url = BASE_URL + path
        r = self.fetch(url).html
        items = r.find('ul.award2019-rstlst__list', first=True)
        items = items.find('li.award2019-rstlst__item')
        for item in items:
            self.parse_item(item, tag)

    def parse_item(self, item, tag):
        a = item.find('a.award2019-rstlst__target', first=True)
        url = a.attrs['href']
        self.add(url, tag)
