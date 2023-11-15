"""Added order table

Revision ID: b18ceac86881
Revises: 40dd78eb7866
Create Date: 2023-11-15 13:18:25.458912

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b18ceac86881'
down_revision: Union[str, None] = '40dd78eb7866'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
