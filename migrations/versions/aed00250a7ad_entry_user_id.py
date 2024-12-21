"""entry user_id

Revision ID: aed00250a7ad
Revises: ec592c9f0280
Create Date: 2024-01-03 13:11:54.022603

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'aed00250a7ad'
down_revision: Union[str, None] = 'ec592c9f0280'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_entries_user_id'), ['user_id'], unique=False)
        batch_op.create_foreign_key('entry_user_id', 'users', ['user_id'], ['id'])

    op.execute(
        'update entries set user_id = f.user_id from feeds f where entries.feed_id = f.id')

    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.alter_column('user_id', nullable=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.drop_constraint('entry_user_id', type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_entries_user_id'))
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###