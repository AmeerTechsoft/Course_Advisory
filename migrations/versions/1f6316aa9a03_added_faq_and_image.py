"""added faq and image.

Revision ID: 1f6316aa9a03
Revises: b8d735afba82
Create Date: 2023-06-11 12:20:46.756435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f6316aa9a03'
down_revision = 'b8d735afba82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lecturer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=255), nullable=True))

    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('image')

    with op.batch_alter_table('lecturer', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
