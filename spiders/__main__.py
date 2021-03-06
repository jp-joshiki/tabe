import click
import logging
from tabe import create_basic_app
from flask.cli import FlaskGroup
from .tabelog import TabelogSpider
from .tabelog_100_top_2017 import Tabelog100Top2017Spider
from .tabelog_100_top_2018 import Tabelog100Top2018Spider
from .tabelog_award_2017 import TabelogAward2017Spider
from .tabelog_award_2018 import TabelogAward2018Spider
from .tabelog_award_2019 import TabelogAward2019Spider


def _create_app(_):
    app = create_basic_app()
    return app


@click.group(cls=FlaskGroup, create_app=_create_app)
def cli():
    format_ = '%(asctime)s %(levelname)-8s [%(name)s] %(message)s'
    logging.basicConfig(format=format_, level=logging.INFO)


@cli.command()
@click.argument('spider')
def run(spider):
    mapping = dict(
        tabelog=TabelogSpider,
        tabelog_100_top_2017=Tabelog100Top2017Spider,
        tabelog_100_top_2018=Tabelog100Top2018Spider,
        tabelog_award_2017=TabelogAward2017Spider,
        tabelog_award_2018=TabelogAward2018Spider,
        tabelog_award_2019=TabelogAward2019Spider,
    )
    spider = mapping.get(spider)
    if spider:
        spider().run()
    else:
        print('Spider not exist')


if __name__ == '__main__':
    cli()
