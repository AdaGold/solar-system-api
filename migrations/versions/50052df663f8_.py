"""empty message

Revision ID: 50052df663f8
Revises: 
Create Date: 2021-10-25 14:21:27.565983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50052df663f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('mythology', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###