"""deleted surname column

Revision ID: 12cc04d066a9
Revises: 2e3499a954c7
Create Date: 2021-09-11 18:25:19.683161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12cc04d066a9'
down_revision = '2e3499a954c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'surname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('surname', sa.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###
