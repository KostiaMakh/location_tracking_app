"""new

Revision ID: 45a37e6c402a
Revises: 776c98f72c81
Create Date: 2023-08-30 10:57:09.714869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45a37e6c402a'
down_revision: Union[str, None] = '776c98f72c81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('domain', sa.Column('ttttt', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('domain', 'ttttt')
    # ### end Alembic commands ###
