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
    from tabe.models import Restaurant, TabelogRestaurant, db

    entries = [
        'michelin_2018',
        'tabelog_100_top_2017',
        'tabelog_award_2017',
        'tabelog_award_2018',
        'tabelog_award_2019',
    ]
    for entry in entries:
        path = f'./data/{entry}.json'
        with open(path, 'r') as f:
            data = json.load(f)
        for piece in data:
            tabelog_url = piece['tabelog_url']
            tabelog_id = int(tabelog_url.split('/')[-2])

            t_res = TabelogRestaurant.query.filter_by(id=tabelog_id).first()
            if not t_res:
                t_res = TabelogRestaurant(id=tabelog_id, source_url=tabelog_url)
                db.session.add(t_res)
                db.session.commit()

            res = Restaurant.query.filter_by(tabelog_restaurant_id=t_res.id).first()
            if not res:
                res = Restaurant(tabelog_restaurant_id=t_res.id)
                db.session.add(res)
                db.session.commit()
            res.append_tags(piece['tags'])
            db.session.add(res)
            db.session.commit()
            print(piece['tabelog_url'])
            print(res.tags)


if __name__ == '__main__':
    cli()
