"""Added order table

Revision ID: 083f760d31fd
Revises: b18ceac86881
Create Date: 2023-11-15 13:24:09.256161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '083f760d31fd'
down_revision: Union[str, None] = 'b18ceac86881'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
