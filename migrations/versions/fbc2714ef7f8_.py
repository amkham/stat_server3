"""empty message

Revision ID: fbc2714ef7f8
Revises: 
Create Date: 2019-05-18 04:41:45.837548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbc2714ef7f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('locations_oktmo_uindex', table_name='locations')
    op.create_unique_constraint(None, 'locations', ['oktmo'])
    op.drop_index('statistic_id_uindex', table_name='statistic')
    op.create_unique_constraint(None, 'statistic', ['id'])
    op.drop_index('subject_kod_uindex', table_name='subject')
    op.create_unique_constraint(None, 'subject', ['kod'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subject', type_='unique')
    op.create_index('subject_kod_uindex', 'subject', ['kod'], unique=True)
    op.drop_constraint(None, 'statistic', type_='unique')
    op.create_index('statistic_id_uindex', 'statistic', ['id'], unique=True)
    op.drop_constraint(None, 'locations', type_='unique')
    op.create_index('locations_oktmo_uindex', 'locations', ['oktmo'], unique=True)
    # ### end Alembic commands ###
