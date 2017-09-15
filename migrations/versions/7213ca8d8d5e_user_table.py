"""user_table

Revision ID: 7213ca8d8d5e
Revises: a007c489b660
Create Date: 2017-09-14 00:29:23.329572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7213ca8d8d5e'
down_revision = 'a007c489b660'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
