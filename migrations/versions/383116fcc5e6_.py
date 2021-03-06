"""empty message

Revision ID: 383116fcc5e6
Revises: 801ff1cab210
Create Date: 2019-05-04 01:39:11.943847

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '383116fcc5e6'
down_revision = '801ff1cab210'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'accounts', ['id'])
    op.add_column('businesses', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.add_column('businesses', sa.Column('modified_on', sa.DateTime(), nullable=True))
    op.create_unique_constraint(None, 'businesses', ['id'])
    op.drop_column('businesses', 'created_at')
    op.drop_column('businesses', 'modified_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('businesses', sa.Column('modified_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('businesses', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'businesses', type_='unique')
    op.drop_column('businesses', 'modified_on')
    op.drop_column('businesses', 'created_on')
    op.drop_constraint(None, 'accounts', type_='unique')
    # ### end Alembic commands ###
