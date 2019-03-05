import json

from requests_html import HTMLSession

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0'


class BaseSpider:
    data = {}
    target = 'data.json'
    session = HTMLSession()

    def run(self):
        raise NotImplemented

    def fetch(self, url):
        self.session.headers.update({'user_agent': USER_AGENT})
        return self.session.get(url)

    def add(self, url, tag):
        prev = self.data.get(url)
        if prev:
            prev['tags'] = prev['tags'] + [tag]
            self.data[url] = prev
        else:
            self.data[url] = dict(tabelog_url=url, tags=[tag])
        print(self.data[url])

    def store(self):
        with open(self.target, 'w') as f:
            data = list(self.data.values())
            data = sorted(data, key=lambda x: x['tabelog_url'])
            json.dump(data, f, indent=4)

    # def parse_tabelog(self, url, tags):
    #     id_ = url.split('/')[-2]
    #     r = self.fetch(url).html
    #     name = r.find('h2.display-name', first=True).text.strip()
    #     rate = r.find('span.rdheader-rating__score-val-dtl', first=True)
    #     try:
    #         rate = float(rate.text.strip())
    #     except ValueError:
    #         rate = None
    #     address = r.find('p.rstinfo-table__address', first=True).text.strip()
    #     images = r.find('p.rstdtl-top-postphoto__photo')
    #     images = [x.find('a', first=True).attrs['href'] for x in images]
    #     try:
    #         location = r.find('p.rstinfo-actions__btn',
    #                           containing='印刷ページを表示',
    #                           first=True) \
    #             .find('a', first=True).attrs['data-print-url']
    #         location = re.search('lat=(.*)&lng=(.*)&rcd', location)
    #         lat = float(location.group(1))
    #         lng = float(location.group(2))
    #     except AttributeError:
    #         lat = None
    #         lng = None
    #
    #     # ～￥999, ￥1,000～￥1,999
    #     def parse_cost(xpath):
    #         from_ = to = None
    #         try:
    #             text = r.find(xpath, first=True).text
    #         except AttributeError:
    #             return from_, to
    #         try:
    #             v = text.split('～')[0]
    #             v = v.replace('￥', '').replace(',', '')
    #             from_ = int(v)
    #         except ValueError:
    #             pass
    #         try:
    #             v = text.split('～')[1]
    #             v = v.replace('￥', '').replace(',', '')
    #             to = int(v)
    #         except ValueError:
    #             pass
    #         return from_, to
    #
    #     tabelog_lunch_price_min, tabelog_lunch_price_max = parse_cost(
    #         'p.rdheader-budget__icon--lunch > span > a'
    #     )
    #     tabelog_dinner_price_min, tabelog_dinner_price_max = parse_cost(
    #         'p.rdheader-budget__icon--dinner > span > a'
    #     )
    #     try:
    #         tabelog_lunch_rate = float(
    #             r.find('span.rdheader-rating__time-icon--lunch > em',
    #                    first=True).text)
    #     except ValueError:
    #         tabelog_lunch_rate = None
    #     try:
    #         tabelog_dinner_rate = float(
    #             r.find('span.rdheader-rating__time-icon--dinner > em',
    #                    first=True).text)
    #     except ValueError:
    #         tabelog_dinner_rate = None
    #
    #     try:
    #         homepage = r.find('p.homepage > a', first=True).attrs['href']
    #     except AttributeError:
    #         homepage = None
    #     try:
    #         tel = r.find('p.rstdtl-side-yoyaku__tel-number', first=True).text
    #     except AttributeError:
    #         tel = None
    #
    #     category_list = r.xpath("//tr[th='ジャンル']/td/span")[0].text \
    #         .replace('（その他）', '').split('、')
    #     categories = []
    #     for item in category_list:
    #         src = Category.query.filter_by(name_ja=item).first()
    #         if not src:
    #             src = Category(name_ja=item)
    #             with db.auto_commit():
    #                 db.session.add(src)
    #         categories.append(src)
    #
    #     try:
    #         offdays = r.find('dd#short-comment', first=True).text
    #         offdays = [x for x in Offday.query.all() if x.name_ja in offdays]
    #     except AttributeError:
    #         offdays = list()
    #
    #     data = dict(
    #         name=name,
    #         url=homepage,
    #         tel=tel,
    #         tabelog_id=id_,
    #         tabelog_url=url,
    #         tabelog_rate=rate,
    #         tabelog_address=address,
    #         images=json.dumps(images),
    #         lat=lat,
    #         lng=lng,
    #
    #         tabelog_lunch_rate=tabelog_lunch_rate,
    #         tabelog_lunch_price_min=tabelog_lunch_price_min,
    #         tabelog_lunch_price_max=tabelog_lunch_price_max,
    #         tabelog_dinner_rate=tabelog_dinner_rate,
    #         tabelog_dinner_price_min=tabelog_dinner_price_min,
    #         tabelog_dinner_price_max=tabelog_dinner_price_max,
    #     )
    #     self.store(tag_ids=tags, categories=categories,
    #                offdays=offdays, **data)
