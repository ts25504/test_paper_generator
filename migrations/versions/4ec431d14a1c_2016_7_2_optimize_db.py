"""2016-7-2-optimize-db

Revision ID: 4ec431d14a1c
Revises: 1b749564871d
Create Date: 2016-07-02 15:36:13.025135

"""

# revision identifiers, used by Alembic.
revision = '4ec431d14a1c'
down_revision = '1b749564871d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'test_paper', 'subject', ['subject'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'test_paper', type_='foreignkey')
    ### end Alembic commands ###