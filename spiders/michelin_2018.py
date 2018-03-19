from ._base import BaseSpider
from tabe.models.tag import (
    MICHELIN_2018,
    MICHELIN_2018_1STAR,
    MICHELIN_2018_2STAR,
    MICHELIN_2018_3STAR,
    MICHELIN_2018_BIG_GOURMAND
)


ENTRIES = [
    'http://gm.gnavi.co.jp/restaurant/list/tokyo/',
    'http://gm.gnavi.co.jp/restaurant/list/kyoto/',
    'http://gm.gnavi.co.jp/restaurant/list/osaka/',
]

BASE_URL = 'http://gm.gnavi.co.jp'


# tabelog search: https://tabelog.com/rstLst/?vs=1&sa=&sk=<keyword>
class Michelin2018Spider(BaseSpider):
    def run(self):
        for url in ENTRIES:
            self.parse_list(url)

    def parse_list(self, url):
        r = self.fetch(url).html
        items = r.find('ul#restaurantList > li')
        for item in items:
            url = item.find('a', first=True).attrs['href']
            url = BASE_URL + url
            self.parse_item(url)

        jumps = r.find('ul.pager > li > a')
        for jump in jumps:
            if jump.text == 'Next»':
                url = BASE_URL + jump.attrs['href']
                self.parse_list(url)

    def parse_item(self, url):
        r = self.fetch(url).html
        award_text = r.find('li.rating > span', first=True).text
        if award_text == 'Bib Gourmand':
            award = MICHELIN_2018_BIG_GOURMAND
        elif award_text == 'one star':
            award = MICHELIN_2018_1STAR
        elif award_text == 'two stars':
            award = MICHELIN_2018_2STAR
        elif award_text == 'three stars':
            award = MICHELIN_2018_3STAR
        else:
            return
        name = r.find('div#restaurantName > h2 > span', first=True).text
        if not name:
            name = r.find('div#restaurantName > h2 > em', first=True).text
        gnavi_id = url.split('/')[-2]
        print(f'["{name}", {award}, "{gnavi_id}"]')




