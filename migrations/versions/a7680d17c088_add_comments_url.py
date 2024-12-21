"""add comments_url

Revision ID: a7680d17c088
Revises: efae92e17e62
Create Date: 2024-01-02 11:55:14.371351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7680d17c088'
down_revision: Union[str, None] = 'efae92e17e62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comments_url', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.drop_column('comments_url')

    # ### end Alembic commands ###
