import logging
import json
import re
from pprint import pformat

from requests_html import HTMLSession
from tabe.models import db
from tabe.models import Restaurant, Tag, Offday, Category

USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) '
    'Gecko/20100101 Firefox/57.0'
)


class BaseSpider:
    session = HTMLSession()

    def run(self):
        raise NotImplemented

    def fetch(self, url):
        self.session.headers.update({'user_agent': USER_AGENT})
        return self.session.get(url)

    @staticmethod
    def store(tag_ids, categories, offdays, **data):
        src = None
        tabelog_id = data.get('tabelog_id')
        if tabelog_id:
            src = Restaurant.query.filter_by(tabelog_id=tabelog_id).first()
        if not src:
            src = Restaurant()
        for k, v in data.items():
            setattr(src, k, v)
        src.tags = [Tag.query.get(x) for x in tag_ids]
        src.offdays = offdays
        src.categories = categories
        with db.auto_commit():
            db.session.add(src)
        logging.info(pformat(data))

    def parse_tabelog(self, url, tags):
        id_ = url.split('/')[-2]
        r = self.fetch(url).html
        name = r.find('h2.display-name', first=True).text.strip()
        rate = r.find('span.rdheader-rating__score-val-dtl', first=True)
        try:
            rate = float(rate.text.strip())
        except ValueError:
            rate = None
        address = r.find('p.rstinfo-table__address', first=True).text.strip()
        images = r.find('p.rstdtl-top-postphoto__photo')
        images = [x.find('a', first=True).attrs['href'] for x in images]
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

        tabelog_lunch_price_min, tabelog_lunch_price_max = parse_cost(
            'p.rdheader-budget__icon--lunch > span > a'
        )
        tabelog_dinner_price_min, tabelog_dinner_price_max = parse_cost(
            'p.rdheader-budget__icon--dinner > span > a'
        )
        try:
            tabelog_lunch_rate = float(
                r.find('span.rdheader-rating__time-icon--lunch > em',
                       first=True).text)
        except ValueError:
            tabelog_lunch_rate = None
        try:
            tabelog_dinner_rate = float(
                r.find('span.rdheader-rating__time-icon--dinner > em',
                       first=True).text)
        except ValueError:
            tabelog_dinner_rate = None

        try:
            homepage = r.find('p.homepage > a', first=True).attrs['href']
        except AttributeError:
            homepage = None
        try:
            tel = r.find('p.rstdtl-side-yoyaku__tel-number', first=True).text
        except AttributeError:
            tel = None

        category_list = r.xpath("//tr[th='ジャンル']/td/span")[0].text \
            .replace('（その他）', '').split('、')
        categories = []
        for item in category_list:
            src = Category.query.filter_by(name_ja=item).first()
            if not src:
                src = Category(name_ja=item)
                with db.auto_commit():
                    db.session.add(src)
            categories.append(src)

        try:
            offdays = r.find('dd#short-comment', first=True).text
            offdays = [x for x in Offday.query.all() if x.name_ja in offdays]
        except AttributeError:
            offdays = list()

        data = dict(
            name=name,
            url=homepage,
            tel=tel,
            tabelog_id=id_,
            tabelog_url=url,
            tabelog_rate=rate,
            tabelog_address=address,
            images=json.dumps(images),
            lat=lat,
            lng=lng,

            tabelog_lunch_rate=tabelog_lunch_rate,
            tabelog_lunch_price_min=tabelog_lunch_price_min,
            tabelog_lunch_price_max=tabelog_lunch_price_max,
            tabelog_dinner_rate=tabelog_dinner_rate,
            tabelog_dinner_price_min=tabelog_dinner_price_min,
            tabelog_dinner_price_max=tabelog_dinner_price_max,
        )
        self.store(tag_ids=tags, categories=categories,
                   offdays=offdays, **data)
