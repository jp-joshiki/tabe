import re
import json

from tabe.models import db, TabelogRestaurant
from ._base import BaseSpider


class TabelogSpider(BaseSpider):
    def run(self):
        cursor = 0
        while True:
            items = TabelogRestaurant.query.offset(cursor).limit(500).all()
            if not items:
                break
            for item in items:
                self.crawl_item(item)
            cursor += 500

    def crawl_item(self, item):
        r = self.fetch(item.source_url).html
        name = r.find('h2.display-name', first=True).text.strip()
        try:
            url = r.find('p.homepage > a', first=True).attrs['href']
        except AttributeError:
            url = None
        rate = r.find('span.rdheader-rating__score-val-dtl', first=True)
        try:
            rate = float(rate.text.strip())
        except ValueError:
            rate = None
        address = r.find('p.rstinfo-table__address', first=True).text.strip()
        try:
            tel = r.find('p.rstdtl-side-yoyaku__tel-number', first=True).text
        except AttributeError:
            tel = None
        images = r.find('p.rstdtl-top-postphoto__photo')
        images = [x.find('a', first=True).attrs['href'] for x in images]
        try:
            lunch_rate = float(
                r.find('span.rdheader-rating__time-icon--lunch > em',
                       first=True).text)
        except AttributeError:
            lunch_rate = None
        try:
            dinner_rate = float(
                r.find('span.rdheader-rating__time-icon--dinner > em',
                       first=True).text)
        except AttributeError:
            dinner_rate = None

        # ～￥999, ￥1,000～￥1,999
        def parse_cost(xpath):
            from_ = to = None
            try:
                text = r.find(xpath, first=True).text
            except AttributeError:
                return from_, to
            try:
                v = text.split('～')[0]
                v = v.replace('￥', '').replace(',', '')
                from_ = int(v)
            except ValueError:
                pass
            try:
                v = text.split('～')[1]
                v = v.replace('￥', '').replace(',', '')
                to = int(v)
            except ValueError:
                pass
            return from_, to

        lunch_price_min, lunch_price_max = parse_cost(
            'p.rdheader-budget__icon--lunch > span > a'
        )
        dinner_price_min, dinner_price_max = parse_cost(
            'p.rdheader-budget__icon--dinner > span > a'
        )

        try:
            location = r.find('p.rstinfo-actions__btn',
                              containing='印刷ページを表示',
                              first=True) \
                .find('a', first=True).attrs['data-print-url']
            location = re.search('lat=(.*)&lng=(.*)&rcd', location)
            lat = float(location.group(1))
            lng = float(location.group(2))
        except AttributeError:
            lat = None
            lng = None

        item.name = name
        item.url = url
        item.rate = rate
        item.address = address
        item.tel = tel
        item.images = json.dumps(images)
        item.lunch_rate = lunch_rate
        item.dinner_rate = dinner_rate
        item.lunch_price_min = lunch_price_min
        item.lunch_price_max = lunch_price_max
        item.dinner_price_min = dinner_price_min
        item.dinner_price_max = dinner_price_max
        item.lat = lat
        item.lng = lng

        db.session.add(item)
        db.session.commit()

        print(name)
