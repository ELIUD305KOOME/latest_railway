"""friday

Revision ID: a6fa7846aea8
Revises: 6b50f2fec66f
Create Date: 2024-12-21 00:17:36.593768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6fa7846aea8'
down_revision = '6b50f2fec66f'
branch_labels = None
depends_on = None




def upgrade():
    # Drop the bookings table
    op.drop_table('bookings')


