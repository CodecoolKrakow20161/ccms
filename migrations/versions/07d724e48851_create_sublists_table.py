"""Create sublists table

Revision ID: 07d724e48851
Revises: 6058f666ef8a
Create Date: 2017-03-21 14:50:52.258817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07d724e48851'
down_revision = '6058f666ef8a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'sublists',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False, unique=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('archived_at', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default='now()'),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default='now()')
    )


def downgrade():
    op.drop_table('sublists')
