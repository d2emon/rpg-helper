"""Basic damage

Revision ID: b224e36e8b59
Revises: 1914d6a37791
Create Date: 2017-02-12 13:40:24.397283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b224e36e8b59'
down_revision = '1914d6a37791'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'basic_damage',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.Integer, index=True, unique=True),
        sa.Column('thrust_dice', sa.Integer),
        sa.Column('thrust_mod', sa.Integer),
        sa.Column('swing_dice', sa.Integer),
        sa.Column('swing_mod', sa.Integer),
    )


def downgrade():
    op.drop_table('basic_damage')