"""Galaxy table

Revision ID: 0c83d0e69bec
Revises: ad9818007315
Create Date: 2017-09-19 14:07:29.275007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c83d0e69bec'
down_revision = 'ad9818007315'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('galaxy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=False),
    sa.Column('description', sa.UnicodeText(), nullable=True),
    sa.Column('world_id', sa.Integer(), nullable=True),

    sa.ForeignKeyConstraint(['world_id'], ['world.id'], ),
    sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('galaxy')
    # ### end Alembic commands ###
