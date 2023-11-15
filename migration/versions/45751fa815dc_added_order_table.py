"""Added order table

Revision ID: 45751fa815dc
Revises: a09802a91a5c
Create Date: 2023-11-15 14:52:04.246200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45751fa815dc'
down_revision: Union[str, None] = 'a09802a91a5c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
