"""measurements table

Revision ID: c2f8efb1c93a
Revises: 282b898a0360
Create Date: 2019-01-05 19:04:25.747271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2f8efb1c93a'
down_revision = '282b898a0360'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('measurement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('date_taken', sa.Date(), nullable=False),
    sa.Column('electricity_high_rate_kwh', sa.Float(), nullable=False),
    sa.Column('electricity_low_rate_kwh', sa.Float(), nullable=False),
    sa.Column('gas_m3', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_measurement_date_taken'), 'measurement', ['date_taken'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_measurement_date_taken'), table_name='measurement')
    op.drop_table('measurement')
    # ### end Alembic commands ###
