"""Create character table

Revision ID: e68ba3e7322b
Revises:
Create Date: 2017-02-12 12:00:09.513413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e68ba3e7322b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'character',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(5), nullable=False),
        sa.Column('description', sa.Unicode(200))
    )


def downgrade():
    op.drop_table('character')
