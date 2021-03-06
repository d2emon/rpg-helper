"""planet_image

Revision ID: 8076d8002cd5
Revises: 87af9ace9e7c
Create Date: 2017-09-24 19:08:14.467774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8076d8002cd5'
down_revision = '87af9ace9e7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet_type', sa.Column('image', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planet_type', 'image')
    # ### end Alembic commands ###
