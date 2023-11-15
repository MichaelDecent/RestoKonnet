"""removed a column

Revision ID: c471c0d04c82
Revises: 083f760d31fd
Create Date: 2023-11-15 13:30:17.824794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c471c0d04c82'
down_revision: Union[str, None] = '083f760d31fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
