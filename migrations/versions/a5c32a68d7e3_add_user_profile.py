"""add user profile

Revision ID: a5c32a68d7e3
Revises: 1237bc28d6fa
Create Date: 2016-03-14 11:44:45.866794

"""

# revision identifiers, used by Alembic.
revision = 'a5c32a68d7e3'
down_revision = '1237bc28d6fa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('location', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'location')
    ### end Alembic commands ###
