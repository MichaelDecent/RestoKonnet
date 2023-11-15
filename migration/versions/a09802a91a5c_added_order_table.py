"""added order table

Revision ID: a09802a91a5c
Revises: 56e1580d5093
Create Date: 2023-11-15 14:27:58.834415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a09802a91a5c'
down_revision: Union[str, None] = '56e1580d5093'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
