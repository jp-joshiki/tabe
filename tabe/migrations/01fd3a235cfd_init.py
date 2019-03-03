"""init

Revision ID: 01fd3a235cfd
Revises: 
Create Date: 2019-03-03 23:48:47.071606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01fd3a235cfd'
down_revision = None
branch_labels = ('default',)
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tabelog_url', sa.String(length=300), nullable=False),
    sa.Column('tags', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tabelog_url')
    )
    op.create_table('tabelog_restaurant',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('source_url', sa.String(length=300), nullable=False),
    sa.Column('url', sa.String(length=300), nullable=True),
    sa.Column('rate', sa.Float(), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('tel', sa.String(length=100), nullable=True),
    sa.Column('images', sa.String(), nullable=True),
    sa.Column('lunch_rate', sa.Float(), nullable=True),
    sa.Column('dinner_rate', sa.Float(), nullable=True),
    sa.Column('lunch_price_min', sa.Integer(), nullable=True),
    sa.Column('lunch_price_max', sa.Integer(), nullable=True),
    sa.Column('dinner_price_min', sa.Integer(), nullable=True),
    sa.Column('dinner_price_max', sa.Integer(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lng', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('source_url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tabelog_restaurant')
    op.drop_table('restaurant')
    # ### end Alembic commands ###
