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
