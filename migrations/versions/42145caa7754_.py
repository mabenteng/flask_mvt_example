"""empty message

Revision ID: 42145caa7754
Revises: 8a3a61eb546a
Create Date: 2021-06-21 17:40:59.762370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42145caa7754'
down_revision = '8a3a61eb546a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('second',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=True),
    sa.Column('pwd', sa.String(length=400), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('second')
    # ### end Alembic commands ###
