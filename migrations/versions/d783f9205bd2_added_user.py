"""added user

Revision ID: d783f9205bd2
Revises: f16ba57edd34
Create Date: 2023-07-26 10:49:42.585217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd783f9205bd2'
down_revision = 'f16ba57edd34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender', sa.String(length=100), nullable=False),
    sa.Column('receiver', sa.String(length=100), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('FAQ',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=500), nullable=False),
    sa.Column('answer', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Lecturer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('staff_id', sa.String(length=20), nullable=False),
    sa.Column('firstname', sa.String(length=20), nullable=False),
    sa.Column('lastname', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('profile_image', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('staff_id')
    )
    op.create_table('Students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('matric_no', sa.String(length=20), nullable=False),
    sa.Column('firstname', sa.String(length=20), nullable=False),
    sa.Column('lastname', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('level', sa.String(length=6), nullable=False),
    sa.Column('profile_image', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('matric_no')
    )
    op.create_table('opnions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profession', sa.String(length=500), nullable=False),
    sa.Column('answer', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('faq')
    op.drop_table('student')
    op.drop_table('lecturer')
    op.drop_table('opinion')
    op.drop_table('chat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sender', sa.VARCHAR(length=100), nullable=False),
    sa.Column('receiver', sa.VARCHAR(length=100), nullable=False),
    sa.Column('message', sa.TEXT(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opinion',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('profession', sa.VARCHAR(length=500), nullable=False),
    sa.Column('answer', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lecturer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('profile_image', sa.VARCHAR(length=255), nullable=True),
    sa.Column('staff_id', sa.VARCHAR(length=20), nullable=False),
    sa.Column('firstname', sa.VARCHAR(length=20), nullable=False),
    sa.Column('lastname', sa.VARCHAR(length=20), nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARCHAR(length=60), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('staff_id')
    )
    op.create_table('student',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('profile_image', sa.VARCHAR(length=255), nullable=True),
    sa.Column('matric_no', sa.VARCHAR(length=20), nullable=False),
    sa.Column('firstname', sa.VARCHAR(length=20), nullable=False),
    sa.Column('lastname', sa.VARCHAR(length=20), nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARCHAR(length=60), nullable=False),
    sa.Column('level', sa.VARCHAR(length=6), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('matric_no')
    )
    op.create_table('faq',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('question', sa.VARCHAR(length=500), nullable=False),
    sa.Column('answer', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    op.drop_table('opnions')
    op.drop_table('Students')
    op.drop_table('Lecturer')
    op.drop_table('FAQ')
    op.drop_table('Chat')
    # ### end Alembic commands ###