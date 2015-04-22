"""initial migration

Revision ID: 4af7bebc7b8e
Revises: 42e8a0643552
Create Date: 2015-04-22 20:59:04.553732

"""

# revision identifiers, used by Alembic.
revision = '4af7bebc7b8e'
down_revision = '42e8a0643552'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_paper', sa.Column('name', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test_paper', 'name')
    ### end Alembic commands ###