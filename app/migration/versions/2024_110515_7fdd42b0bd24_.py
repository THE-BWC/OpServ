"""empty message

Revision ID: 7fdd42b0bd24
Revises: 482c23583e52
Create Date: 2024-11-05 15:20:20.036421

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = "7fdd42b0bd24"
down_revision = "482c23583e52"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "enlistment_applications",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("submitted_form", mysql.LONGTEXT(), nullable=False),
        sa.Column("status", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_user_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.Column("edited_user_id", sa.Integer(), nullable=True),
        sa.Column(
            "edited_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["created_user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["edited_user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="cascade"),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("billets", schema=None) as batch_op:
        batch_op.alter_column(
            "retired",
            existing_type=mysql.SMALLINT(display_width=6),
            type_=sa.Boolean(),
            existing_nullable=False,
        )

    with op.batch_alter_table("games", schema=None) as batch_op:
        batch_op.alter_column(
            "retired",
            existing_type=mysql.INTEGER(display_width=11),
            type_=sa.Boolean(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "opsec",
            existing_type=mysql.INTEGER(display_width=11),
            type_=sa.Boolean(),
            existing_nullable=False,
        )

    with op.batch_alter_table("operation_types", schema=None) as batch_op:
        batch_op.alter_column(
            "live_fire",
            existing_type=mysql.INTEGER(display_width=11),
            type_=sa.Boolean(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "retired",
            existing_type=mysql.INTEGER(display_width=11),
            type_=sa.Boolean(),
            existing_nullable=False,
        )

    with op.batch_alter_table("operations", schema=None) as batch_op:
        batch_op.alter_column(
            "is_completed",
            existing_type=mysql.INTEGER(display_width=11),
            type_=sa.Boolean(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "is_opsec",
            existing_type=mysql.INTEGER(display_width=11),
            type_=sa.Boolean(),
            existing_nullable=False,
        )

    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(sa.Column("email_verified", sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column("signed_sop", sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_column("signed_sop")
        batch_op.drop_column("email_verified")

    with op.batch_alter_table("operations", schema=None) as batch_op:
        batch_op.alter_column(
            "is_opsec",
            existing_type=sa.Boolean(),
            type_=mysql.INTEGER(display_width=11),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "is_completed",
            existing_type=sa.Boolean(),
            type_=mysql.INTEGER(display_width=11),
            existing_nullable=False,
        )

    with op.batch_alter_table("operation_types", schema=None) as batch_op:
        batch_op.alter_column(
            "retired",
            existing_type=sa.Boolean(),
            type_=mysql.INTEGER(display_width=11),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "live_fire",
            existing_type=sa.Boolean(),
            type_=mysql.INTEGER(display_width=11),
            existing_nullable=False,
        )

    with op.batch_alter_table("games", schema=None) as batch_op:
        batch_op.alter_column(
            "opsec",
            existing_type=sa.Boolean(),
            type_=mysql.INTEGER(display_width=11),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "retired",
            existing_type=sa.Boolean(),
            type_=mysql.INTEGER(display_width=11),
            existing_nullable=False,
        )

    with op.batch_alter_table("billets", schema=None) as batch_op:
        batch_op.alter_column(
            "retired",
            existing_type=sa.Boolean(),
            type_=mysql.SMALLINT(display_width=6),
            existing_nullable=False,
        )

    op.drop_table("enlistment_applications")
    # ### end Alembic commands ###