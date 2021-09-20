"""portfolio table created

Revision ID: f50cf8a76f65
Revises: 0c872576e8bb
Create Date: 2021-09-13 13:01:42.998509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f50cf8a76f65'
down_revision = '0c872576e8bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('portfolio_img', sa.String(length=100), nullable=True),
    sa.Column('portfolio_name', sa.String(length=100), nullable=True),
    sa.Column('portfolio_link', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolio')
    # ### end Alembic commands ###
