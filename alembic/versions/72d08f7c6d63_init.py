"""Init

Revision ID: 72d08f7c6d63
Revises: 
Create Date: 2025-04-20 15:12:40.267834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '72d08f7c6d63'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('name', sa.String(length=49), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tags_id'), 'tags', ['id'], unique=True)
    op.create_index(op.f('ix_tags_name'), 'tags', ['name'], unique=True)
    op.create_table('users',
    sa.Column('username', sa.String(length=49), nullable=False),
    sa.Column('password', sa.String(length=155), nullable=False),
    sa.Column('unblock_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('pages',
    sa.Column('name', sa.String(length=49), nullable=False),
    sa.Column('about', sa.String(length=1024), nullable=True),
    sa.Column('is_private', sa.Boolean(), nullable=False),
    sa.Column('unblock_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pages_id'), 'pages', ['id'], unique=True)
    op.create_index(op.f('ix_pages_name'), 'pages', ['name'], unique=True)
    op.create_table('users_data',
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('tg_nickname', sa.String(), nullable=True),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_data_email'), 'users_data', ['email'], unique=True)
    op.create_index(op.f('ix_users_data_id'), 'users_data', ['id'], unique=True)
    op.create_index(op.f('ix_users_data_tg_nickname'), 'users_data', ['tg_nickname'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_data_tg_nickname'), table_name='users_data')
    op.drop_index(op.f('ix_users_data_id'), table_name='users_data')
    op.drop_index(op.f('ix_users_data_email'), table_name='users_data')
    op.drop_table('users_data')
    op.drop_index(op.f('ix_pages_name'), table_name='pages')
    op.drop_index(op.f('ix_pages_id'), table_name='pages')
    op.drop_table('pages')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_tags_name'), table_name='tags')
    op.drop_index(op.f('ix_tags_id'), table_name='tags')
    op.drop_table('tags')
    # ### end Alembic commands ###
