"""init

Revision ID: ac2954aeac0f
Revises: 
Create Date: 2022-04-12 20:50:13.552106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac2954aeac0f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "test",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String, nullable=False)
    )


def downgrade():
    op.drop_table("test")
