"""empty message

Revision ID: 72ab1e11a957
Revises: ddfe0536f53b
Create Date: 2018-05-09 20:02:57.648965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72ab1e11a957'
down_revision = 'ddfe0536f53b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('world', sa.Column('img', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('world', 'img')
    # ### end Alembic commands ###
