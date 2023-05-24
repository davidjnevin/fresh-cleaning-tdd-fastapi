"""create_main_tables
Revision ID: da0f3a58a75e
Revises:
Create Date: 2023-05-24 09:11:58.007599
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = 'da0f3a58a75e'
down_revision = None
branch_labels = None
depends_on = None


def create_cleanings_table() -> None:
    op.create_table(
        "cleanings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )

def upgrade() -> None:
    create_cleanings_table()

def downgrade() -> None:
    op.drop_table("cleanings")
