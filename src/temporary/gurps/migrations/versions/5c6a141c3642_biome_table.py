"""biome table

Revision ID: 5c6a141c3642
Revises: e6287e300888
Create Date: 2017-02-14 03:01:29.736374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c6a141c3642'
down_revision = 'e6287e300888'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'biome',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('wilderness_id', sa.Integer()),
        sa.Column('encounter_id', sa.Integer()),
        sa.Column('description', sa.String()),
        sa.ForeignKeyConstraint(['encounter_id'], ['encounter_table.id'], ),
        sa.ForeignKeyConstraint(['wilderness_id'], ['wilderness.id'], ),
    )


def downgrade():
    op.drop_table('biome')