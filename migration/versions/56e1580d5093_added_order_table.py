"""added order table

Revision ID: 56e1580d5093
Revises: 030622a65e44
Create Date: 2023-11-15 13:46:55.624636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56e1580d5093'
down_revision: Union[str, None] = '030622a65e44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
