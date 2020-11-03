"""empty message

Revision ID: 000d997bd34e
Revises: 2af05f61883b
Create Date: 2020-11-02 17:19:19.023971

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '000d997bd34e'
down_revision = '2af05f61883b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('description', sa.Text(), nullable=False))
    op.alter_column('card', 'card_service',
                existing_type=mysql.VARCHAR(length=50),
                type_=sa.Integer(),
                existing_nullable=False)
    op.alter_column('card', 'short_description',
                existing_type=mysql.TEXT(),
                type_=sa.String(length=80),
                existing_nullable=False)
        # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('card', 'short_description',
                existing_type=sa.String(length=80),
                type_=mysql.TEXT(),
                existing_nullable=False)
op.alter_column('card', 'card_service',
                existing_type=sa.Integer(),
                type_=mysql.VARCHAR(length=50),
                existing_nullable=False)
    op.drop_column('card', 'description')
    # ### end Alembic commands ###