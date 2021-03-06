"""Temp_remove_client_secret"

Revision ID: 13948860312b
Revises: 0f7142142e11
Create Date: 2018-12-13 01:55:10.480176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13948860312b'
down_revision = '0f7142142e11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('client_secret')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('client_secret', sa.VARCHAR(length=256), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
