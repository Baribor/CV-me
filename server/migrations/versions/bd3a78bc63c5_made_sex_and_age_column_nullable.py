"""made sex and age column nullable

Revision ID: bd3a78bc63c5
Revises: 65f28fce9aa7
Create Date: 2024-02-21 16:08:51.662687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd3a78bc63c5'
down_revision: Union[str, None] = '65f28fce9aa7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'age',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('users', 'sex',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'sex',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('users', 'age',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
