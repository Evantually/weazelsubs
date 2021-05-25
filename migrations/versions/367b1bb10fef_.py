"""empty message

Revision ID: 367b1bb10fef
Revises: 
Create Date: 2021-05-25 08:02:16.074439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '367b1bb10fef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sub_id', sa.String(length=12), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('active_status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscription')
    # ### end Alembic commands ###
