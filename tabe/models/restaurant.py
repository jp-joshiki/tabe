import json
from sqlalchemy import Column
from sqlalchemy import Integer, Text, String

from . import db


class Restaurant(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    tabelog_url = Column(String(300), unique=True, nullable=False)

    tags = Column(Text)

    def append_tags(self, tags):
        if self.tags:
            prev = json.loads(self.tags)
        else:
            prev = []
        for tag in tags:
            if tag not in prev:
                prev.append(tag)
        self.tags = json.dumps(prev)
