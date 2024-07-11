"""empty message

Revision ID: 6355730115bc
Revises: 
Create Date: 2024-07-10 12:20:20.376738

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6355730115bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.Column('edited_user_id', sa.Integer(), nullable=True),
    sa.Column('edited_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.ForeignKeyConstraint(['created_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['edited_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
