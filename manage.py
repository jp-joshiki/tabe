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


@cli.command(help='Update db')
def update_db():
    from tabe.models import Tag, Offday
    Tag.update()
    Offday.update()


if __name__ == '__main__':
    cli()
