"""empty message

Revision ID: 133744c6fd3e
Revises: 1a186a9c5d50
Create Date: 2020-11-05 04:09:56.010223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '133744c6fd3e'
down_revision = '1a186a9c5d50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ForeignCurrencies', sa.Column('created_date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ForeignCurrencies', 'created_date')
    # ### end Alembic commands ###
