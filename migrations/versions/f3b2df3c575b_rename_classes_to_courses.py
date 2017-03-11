"""rename_classes_to_courses

Revision ID: f3b2df3c575b
Revises: 3109f5b15463
Create Date: 2017-03-11 22:20:08.851047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3b2df3c575b'
down_revision = '3109f5b15463'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('classes', 'courses')


def downgrade():
    op.rename_table('courses', 'classes')
