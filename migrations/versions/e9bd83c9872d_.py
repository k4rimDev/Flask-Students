"""empty message

Revision ID: e9bd83c9872d
Revises: 85fd6d926bea
Create Date: 2023-08-23 20:49:26.760403

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e9bd83c9872d'
down_revision = '85fd6d926bea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('students', 'bio',
               existing_type=mysql.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('students', 'bio',
               existing_type=mysql.TEXT(),
               nullable=True)
    # ### end Alembic commands ###