"""empty message

Revision ID: 8a1a7c0163ff
Revises: 71267147391a
Create Date: 2023-04-11 23:48:35.511861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a1a7c0163ff'
down_revision = '71267147391a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currencies',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('symbol', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('members',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('group_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('icons', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('member_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('configs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('currency_default_id', sa.INTEGER(), nullable=True),
    sa.Column('member_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['currency_default_id'], ['currencies.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.Text(), nullable=True),
    sa.Column('value', sa.INTEGER(), nullable=True),
    sa.Column('category_id', sa.INTEGER(), nullable=True),
    sa.Column('currency_id', sa.INTEGER(), nullable=True),
    sa.Column('member_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['currency_id'], ['currencies.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('configs')
    op.drop_table('categories')
    op.drop_table('members')
    op.drop_table('groups')
    op.drop_table('currencies')
    # ### end Alembic commands ###