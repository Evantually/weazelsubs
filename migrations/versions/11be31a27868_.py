"""empty message

Revision ID: 11be31a27868
Revises: fe2c9ae9153a
Create Date: 2021-05-27 21:16:00.937033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11be31a27868'
down_revision = 'fe2c9ae9153a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscription', sa.Column('paid_sub', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subscription', 'paid_sub')
    # ### end Alembic commands ###
