import click
from tabe import create_app
from flask.cli import FlaskGroup
from flask_alembic import Alembic


def _create_app(_):
    app = create_app()
    Alembic(app)
    return app


@click.group(cls=FlaskGroup, create_app=_create_app)
def cli():
    pass


@cli.command(help='sync restaurants')
def res_sync():
    import json
    from tabe.models import Restaurant, db

    entries = ['michelin_2018', 'tabelog_2017_top_100', 'tabelog_award_2018']
    for entry in entries:
        path = f'./data/{entry}.json'
        with open(path, 'r') as f:
            data = json.load(f)
        for piece in data:
            res = Restaurant.query.filter_by(tabelog_url=piece['tabelog_url']).first()
            if not res:
                res = Restaurant(tabelog_url=piece['tabelog_url'])
            res.append_tags(piece['tags'])
            db.session.add(res)
            db.session.commit()
            print(piece['tabelog_url'])


if __name__ == '__main__':
    cli()
