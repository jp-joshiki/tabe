import logging
import re
from pprint import pformat

from requests_html import HTMLSession
from tabe.models import db
from tabe.models import Restaurant, RestaurantTag

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
    def store(tag_ids, **data):
        src = None
        tabelog_id = data.get('tabelog_id')
        if tabelog_id:
            src = Restaurant.query.filter_by(tabelog_id=tabelog_id).first()
        if not src:
            src = Restaurant()
        for k, v in data.items():
            setattr(src, k, v)
        with db.auto_commit():
            db.session.add(src)
        existing_tag_ids = [x.id for x in src.tags]
        for tag_id in tag_ids:
            if tag_id in existing_tag_ids:
                continue
            r_tag = RestaurantTag(restaurant_id=src.id, tag_id=tag_id)
            with db.auto_commit():
                db.session.add(r_tag)
        logging.info(pformat(data))

    def parse_tabelog(self, url, tags):
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
