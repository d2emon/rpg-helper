"""star_description

Revision ID: c5c418709bfc
Revises: db274dfe98e7
Create Date: 2017-09-22 13:23:38.095309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5c418709bfc'
# down_revision = 'db274dfe98e7'
down_revision = 'c1d2ea6b6746'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('star', sa.Column('description', sa.UnicodeText(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('star', 'description')
    # ### end Alembic commands ###
