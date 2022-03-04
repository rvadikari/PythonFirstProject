"""adding ondelete option to userid in votes table

Revision ID: 565e5af48655
Revises: 3d00bc5cbc5f
Create Date: 2022-03-04 13:41:08.097946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '565e5af48655'
down_revision = '3d00bc5cbc5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('FK__votes__user_id__6FE99F9F', 'votes', type_='foreignkey')
    op.create_foreign_key(None, 'votes', 'users', ['user_id'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.create_foreign_key('FK__votes__user_id__6FE99F9F', 'votes', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
