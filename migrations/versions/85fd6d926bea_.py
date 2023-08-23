"""empty message

Revision ID: 85fd6d926bea
Revises: 
Create Date: 2023-08-23 19:39:24.906682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85fd6d926bea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=False),
    sa.Column('surname', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.String(length=6), nullable=False),
    sa.Column('status', sa.String(length=8), nullable=False),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    # ### end Alembic commands ###
