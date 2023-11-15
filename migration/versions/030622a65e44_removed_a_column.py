"""removed a column

Revision ID: 030622a65e44
Revises: c471c0d04c82
Create Date: 2023-11-15 13:42:41.192963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '030622a65e44'
down_revision: Union[str, None] = 'c471c0d04c82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
