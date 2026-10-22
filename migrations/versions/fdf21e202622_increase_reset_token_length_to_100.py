"""Increase reset_token length to 100
Revision ID: fdf21e202622
Revises: c88465a5432d
Create Date: 2025-06-17 22:37:44.634067
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
revision = 'fdf21e202622'
down_revision = 'c88465a5432d'
branch_labels = None
depends_on = None
def upgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column(
            'reset_token',
            existing_type=mysql.VARCHAR(length=32),
            type_=sa.String(length=100),
            existing_nullable=True
        )
def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column(
            'reset_token',
            existing_type=sa.String(length=100),
            type_=mysql.VARCHAR(length=32),
            existing_nullable=True
        )