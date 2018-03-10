from pprint import pprint

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
        tabelog_id = data.get('tabelog_id')
        src = None
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
        pprint(data)
