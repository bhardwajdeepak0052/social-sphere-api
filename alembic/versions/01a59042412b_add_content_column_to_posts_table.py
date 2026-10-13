"""add content column to posts table

Revision ID: 01a59042412b
Revises: d3734ed5dff1
Create Date: 2026-10-13 16:08:12.260899

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "01a59042412b"
down_revision: Union[str, Sequence[str], None] = "d3734ed5dff1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_Column("posts", "content")
    pass
