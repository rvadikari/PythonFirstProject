"""adding foriegnkey to the post table

Revision ID: f8b215338184
Revises: cef1f023009d
Create Date: 2022-03-03 18:10:09.654497

"""
from tkinter import CASCADE
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8b215338184'
down_revision = 'cef1f023009d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",sa.Column("user_id",sa.Integer,nullable=False))
    op.create_foreign_key('post_users_fk', "posts", referent_table="users", local_cols=[
                          "user_id"], remote_cols=["id"], ondelete=CASCADE)
    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column("posts","user_id")
    pass
