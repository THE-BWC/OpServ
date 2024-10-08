"""empty message

Revision ID: 6a7b24f29bd2
Revises: 2ef9c1e6ad97
Create Date: 2024-09-02 19:21:44.941259

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6a7b24f29bd2'
down_revision = '2ef9c1e6ad97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_activated', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True))
        batch_op.add_column(sa.Column('date_discharged', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('date_discharged')
        batch_op.drop_column('date_activated')

    # ### end Alembic commands ###
