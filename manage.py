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


@cli.command(help='Update db data')
def update_tags():
    from tabe.models import Tag
    Tag.update()


if __name__ == '__main__':
    cli()
