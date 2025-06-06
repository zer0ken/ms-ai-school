"""empty message

Revision ID: 9ad29fc6bb36
Revises: 43c83eb361e6
Create Date: 2025-04-22 16:40:27.500676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ad29fc6bb36'
down_revision = '43c83eb361e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('modified_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_at', sa.DATETIME(), nullable=True))
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###
