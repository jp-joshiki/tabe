"""i18n

Revision ID: 9bbd01cb5fca
Revises: be741bec0f49
Create Date: 2018-03-19 23:36:42.610486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bbd01cb5fca'
down_revision = 'be741bec0f49'
branch_labels = ()
depends_on = None


def upgrade():
    op.add_column('tag', sa.Column('name_en', sa.String(length=100), nullable=True))
    op.add_column('tag', sa.Column('name_cn', sa.String(length=100), nullable=True))


def downgrade():
    op.drop_column('tag', 'name_en')
    op.drop_column('tag', 'name_cn')
