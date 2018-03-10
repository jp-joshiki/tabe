"""init

Revision ID: be741bec0f49
Revises:
Create Date: 2018-03-10 21:56:22.480543

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'be741bec0f49'
down_revision = None
branch_labels = ('default',)
depends_on = None


def upgrade():
    op.create_table(
        'restaurant',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=True),
        sa.Column('tabelog_id', sa.String(length=100), nullable=True),
        sa.Column('tabelog_url', sa.String(length=300), nullable=True),
        sa.Column('tabelog_rate', sa.Float(), nullable=True),
        sa.Column('tabelog_address', sa.Text(), nullable=True),
        sa.Column('images', sa.JSON(), nullable=True),
        sa.Column('lat', sa.Float(), nullable=True),
        sa.Column('lng', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('tabelog_id')
    )
    op.create_table(
        'tag',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name_ja', sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'restaurant_tag',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('restaurant_id', sa.Integer(), nullable=True),
        sa.Column('tag_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
        sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('restaurant_tag')
    op.drop_table('tag')
    op.drop_table('restaurant')
