"""star_image

Revision ID: 6e948a0f2d25
Revises: 7a3aa562c645
Create Date: 2017-09-22 13:28:38.418487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e948a0f2d25'
down_revision = '7a3aa562c645'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('star', sa.Column('image', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('star', 'image')
    # ### end Alembic commands ###
