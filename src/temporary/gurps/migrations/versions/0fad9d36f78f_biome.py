"""biome

Revision ID: 0fad9d36f78f
Revises: b224e36e8b59
Create Date: 2017-02-14 00:28:17.759623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fad9d36f78f'
down_revision = 'b224e36e8b59'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'wilderness',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String),
        sa.Column('chance', sa.Integer),
    )


def downgrade():
    op.drop_table('wilderness')