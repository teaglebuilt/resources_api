"""empty message

Revision ID: 4b6587b98b26
Revises: 158d296b23b8
Create Date: 2019-10-25 20:17:13.589577

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '4b6587b98b26'
down_revision = '158d296b23b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('key', sa.Column('blacklisted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('key', 'blacklisted')
    # ### end Alembic commands ###