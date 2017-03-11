"""create people table

Revision ID: 6058f666ef8a
Revises: f3b2df3c575b
Create Date: 2017-03-11 23:21:31.990699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6058f666ef8a'
down_revision = 'f3b2df3c575b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'people',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(100), nullable=False),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('e-mail', sa.String(255), nullable=False, unique=True),
        sa.Column('phone', sa.String(30), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default='now()'),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default='now()')
    )


def downgrade():
    op.drop_table('people')
