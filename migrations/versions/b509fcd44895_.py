"""empty message

Revision ID: b509fcd44895
Revises: afc8e0a032d1
Create Date: 2019-05-04 17:46:26.064049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b509fcd44895'
down_revision = 'afc8e0a032d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('username', sa.String(length=128), nullable=False))
    op.create_unique_constraint(None, 'accounts', ['username'])
    op.create_unique_constraint(None, 'businesses', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'businesses', type_='unique')
    op.drop_constraint(None, 'accounts', type_='unique')
    op.drop_column('accounts', 'username')
    # ### end Alembic commands ###