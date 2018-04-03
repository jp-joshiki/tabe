"""more data

Revision ID: ef84c87c99e7
Revises: 9bbd01cb5fca
Create Date: 2018-03-29 23:25:26.450279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef84c87c99e7'
down_revision = '9bbd01cb5fca'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_ja', sa.String(length=100), nullable=True),
    sa.Column('name_en', sa.String(length=100), nullable=True),
    sa.Column('name_cn', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name_ja')
    )
    op.create_table('offday',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_ja', sa.String(length=100), nullable=True),
    sa.Column('name_en', sa.String(length=100), nullable=True),
    sa.Column('name_cn', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant_offday',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('offday_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['offday_id'], ['offday.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('restaurant', sa.Column('tabelog_dinner_price_max', sa.Integer(), nullable=True))
    op.add_column('restaurant', sa.Column('tabelog_dinner_price_min', sa.Integer(), nullable=True))
    op.add_column('restaurant', sa.Column('tabelog_dinner_rate', sa.Float(), nullable=True))
    op.add_column('restaurant', sa.Column('tabelog_lunch_price_max', sa.Integer(), nullable=True))
    op.add_column('restaurant', sa.Column('tabelog_lunch_price_min', sa.Integer(), nullable=True))
    op.add_column('restaurant', sa.Column('tabelog_lunch_rate', sa.Float(), nullable=True))
    op.add_column('restaurant', sa.Column('tel', sa.String(length=100), nullable=True))
    op.add_column('restaurant', sa.Column('url', sa.String(length=300), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurant', 'url')
    op.drop_column('restaurant', 'tel')
    op.drop_column('restaurant', 'tabelog_lunch_rate')
    op.drop_column('restaurant', 'tabelog_lunch_price_min')
    op.drop_column('restaurant', 'tabelog_lunch_price_max')
    op.drop_column('restaurant', 'tabelog_dinner_rate')
    op.drop_column('restaurant', 'tabelog_dinner_price_min')
    op.drop_column('restaurant', 'tabelog_dinner_price_max')
    op.drop_table('restaurant_offday')
    op.drop_table('restaurant_category')
    op.drop_table('offday')
    op.drop_table('category')
    # ### end Alembic commands ###