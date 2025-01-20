"""new

Revision ID: 88fed774cae3
Revises: 17d892034744
Create Date: 2024-12-18 13:54:35.648256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88fed774cae3'
down_revision = '17d892034744'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookings', sa.Column('appointment', sa.String(length=25), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bookings', 'appointment')
    # ### end Alembic commands ###
