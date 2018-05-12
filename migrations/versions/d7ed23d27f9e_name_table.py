"""name_table

Revision ID: d7ed23d27f9e
Revises: 8ceb209b22c2
Create Date: 2018-05-12 12:36:09.014163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7ed23d27f9e'
down_revision = '8ceb209b22c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('gender_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gender_id'], ['gender.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('title',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=False),
    sa.Column('gender_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gender_id'], ['gender.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('title')
    op.drop_table('name')
    # ### end Alembic commands ###