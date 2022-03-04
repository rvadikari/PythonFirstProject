"""create a new post table and user table

Revision ID: cef1f023009d
Revises: 
Create Date: 2022-03-03 17:02:57.854598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cef1f023009d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column('id', sa.Integer, primary_key=True, nullable=False), sa.Column(
        'title', sa.String, nullable=False), sa.Column('content', sa.String, nullable=False),
        sa.Column('published', sa.Boolean,
                  nullable=False, server_default='True'),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()))
    op.create_table("users", sa.Column('id', sa.Integer, primary_key=True, nullable=False), sa.Column(
        'email', sa.VARCHAR(50), nullable=False, unique=True), sa.Column('content', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()))

    pass


def downgrade():
    op.drop_table("users")
    op.drop_table("posts")

    pass
