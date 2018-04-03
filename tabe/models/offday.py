from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String

from . import db
from ._utils import I18n
import calendar
import locale


class RestaurantOffday(db.Model):
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    offday_id = Column(Integer, ForeignKey('offday.id'))


class Offday(db.Model):
    id = Column(Integer, primary_key=True)
    name_ja = Column(String(100))
    name_en = Column(String(100))
    name_cn = Column(String(100))

    @staticmethod
    def update():
        locale.setlocale(locale.LC_ALL, 'ja_JP')
        ja_days = [x[:-1] for x in calendar.day_name[:7]] + ['祝日']
        locale.setlocale(locale.LC_ALL, 'en_us')
        en_days = calendar.day_name[:7] + ['Holiday']
        locale.setlocale(locale.LC_ALL, 'zh_tw')
        cn_days = calendar.day_name[:7] + ['休息日']
        for ja, en, cn in zip(ja_days, en_days, cn_days):
            src = Offday.query.filter_by(name_ja=ja).first()
            if not src:
                src = Offday(name_ja=ja, name_en=en, name_cn=cn)
            db.session.add(src)
            db.session.flush()
        db.session.commit()

    def to_dict(self):
        return I18n.complex(self.name_ja, self.name_en, self.name_cn)
