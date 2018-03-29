import os

from fabric.api import env, put, local
from tabe import create_app
from tabe.models import Restaurant, Tag
from flask import json


env.use_ssh_config = True
env.user = 'ubuntu'
env.hosts = ['duan-p0']


def publish():
    local('rm -rf dist')
    app = create_app()
    app.app_context().push()
    grouped_tags = Tag.grouped()
    os.makedirs('./dist', exist_ok=True)
    with open('./dist/grouped_tags.json', 'w') as f:
        json.dump(grouped_tags, f)
    tags = Tag.query.all()
    with open('./dist/tags.json', 'w') as f:
        json.dump(tags, f)
    os.makedirs('./dist/tag_restaurants', exist_ok=True)
    tags = Tag.query.all()
    for tag in tags:
        restaurants = Restaurant.query \
            .filter(Restaurant.tags.any(id=tag.id)) \
            .filter(Restaurant.lat.isnot(None)) \
            .filter(Restaurant.lng.isnot(None)).all()
        with open(f'./dist/tag_restaurants/{tag.id}.json', 'w') as f:
            json.dump(restaurants, f)
    put('./dist/*', '/var/www/tabe')
