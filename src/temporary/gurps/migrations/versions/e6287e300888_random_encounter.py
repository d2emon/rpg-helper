"""random encounter

Revision ID: e6287e300888
Revises: 0fad9d36f78f
Create Date: 2017-02-14 01:54:11.510401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6287e300888'
down_revision = '0fad9d36f78f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('encounter_point',
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('roll', sa.Integer()),
    sa.Column('description', sa.String()),
    )

    op.create_table('encounter_table',
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('description', sa.String()),
    )


def downgrade():
    op.drop_table('encounter_table')
    op.drop_table('encounter_point')