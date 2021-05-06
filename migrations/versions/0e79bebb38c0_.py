"""empty message

Revision ID: 0e79bebb38c0
Revises: d6ada7c7a86e
Create Date: 2021-05-05 19:47:12.633701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e79bebb38c0'
down_revision = 'd6ada7c7a86e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'rental', 'video', ['video_id'], ['video_id'])
    op.create_foreign_key(None, 'rental', 'customer', ['customer_id'], ['customer_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rental', type_='foreignkey')
    op.drop_constraint(None, 'rental', type_='foreignkey')
    # ### end Alembic commands ###
