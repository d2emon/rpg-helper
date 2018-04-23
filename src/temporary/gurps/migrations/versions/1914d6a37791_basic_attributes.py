"""Basic attributes

Revision ID: 1914d6a37791
Revises: e68ba3e7322b
Create Date: 2017-02-12 12:24:07.977036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1914d6a37791'
down_revision = 'e68ba3e7322b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('character', sa.Column('st', sa.Integer, default=10))
    op.add_column('character', sa.Column('dx', sa.Integer, default=10))
    op.add_column('character', sa.Column('iq', sa.Integer, default=10))
    op.add_column('character', sa.Column('ht', sa.Integer, default=10))


def downgrade():
    op.drop_column('character', 'st')
    op.drop_column('character', 'dx')
    op.drop_column('character', 'iq')
    op.drop_column('character', 'ht')
