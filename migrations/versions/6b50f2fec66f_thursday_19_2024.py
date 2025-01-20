"""thursday 19 2024

Revision ID: 6b50f2fec66f
Revises: 88fed774cae3
Create Date: 2024-12-19 20:56:05.163042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b50f2fec66f'
down_revision = '88fed774cae3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookings', sa.Column('status', sa.String(length=255), nullable=True , server_default='pending'))
    op.add_column('bookings', sa.Column('amount_paid', sa.String(length=255), nullable=True , server_default='00.00'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bookings', 'amount_paid')
    op.drop_column('bookings', 'status')
    # ### end Alembic commands ###
