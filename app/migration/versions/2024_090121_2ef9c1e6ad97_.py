"""empty message

Revision ID: 2ef9c1e6ad97
Revises: 1f07b1247550
Create Date: 2024-09-01 21:44:28.824004

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2ef9c1e6ad97"
down_revision = "1f07b1247550"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(sa.Column("password", sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_column("password")

    # ### end Alembic commands ###