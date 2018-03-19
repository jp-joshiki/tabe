import click
import logging
from tabe import create_basic_app
from flask.cli import FlaskGroup
from .tabelog_2017_top_100 import Tabelog2017Top100Spider
from .tabelog_2018 import Tabelog2018Spider
from .michelin_2018 import Michelin2018Spider


def _create_app(_):
    app = create_basic_app()
    return app


@click.group(cls=FlaskGroup, create_app=_create_app)
def cli():
    format_ = '%(asctime)s %(levelname)-8s [%(name)s] %(message)s'
    logging.basicConfig(format=format_, level=logging.INFO)


@cli.command()
def tabelog_2017_top_100():
    Tabelog2017Top100Spider().run()


@cli.command()
def tabelog_2018():
    Tabelog2018Spider().run()


@cli.command()
def michelin_2018():
    Michelin2018Spider().run()


if __name__ == '__main__':
    cli()
