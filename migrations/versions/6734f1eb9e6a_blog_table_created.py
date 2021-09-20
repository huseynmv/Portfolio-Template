"""Blog table created

Revision ID: 6734f1eb9e6a
Revises: f50cf8a76f65
Create Date: 2021-09-14 01:35:35.792577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6734f1eb9e6a'
down_revision = 'f50cf8a76f65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_img', sa.String(length=100), nullable=True),
    sa.Column('blog_name', sa.String(length=100), nullable=True),
    sa.Column('blog_link', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog')
    # ### end Alembic commands ###
