"""empty message

Revision ID: 836093f9f3e4
Revises: 
Create Date: 2024-11-14 00:57:35.479278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '836093f9f3e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=500), nullable=False),
    sa.Column('rol', sa.String(length=100), nullable=False),
    sa.Column('telefono', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehiculo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo_producto', sa.String(length=100), nullable=False),
    sa.Column('matricula', sa.String(length=10), nullable=False),
    sa.Column('transporte', sa.String(length=100), nullable=False),
    sa.Column('kilometraje', sa.Float(), nullable=False),
    sa.Column('oem', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reparacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_chofer_propietario', sa.Integer(), nullable=True),
    sa.Column('vehiculo_id', sa.Integer(), nullable=True),
    sa.Column('fallas', sa.String(length=200), nullable=True),
    sa.Column('diagnostico', sa.String(length=200), nullable=True),
    sa.Column('DTC', sa.String(length=100), nullable=True),
    sa.Column('solucion', sa.String(length=300), nullable=True),
    sa.Column('tecnico_id', sa.Integer(), nullable=True),
    sa.Column('fecha_ingreso', sa.Date(), nullable=True),
    sa.Column('fecha_reparacion', sa.Date(), nullable=True),
    sa.Column('costo_reparacion', sa.Float(), nullable=True),
    sa.Column('monto_cancelado_tecnico', sa.Float(), nullable=True),
    sa.Column('porcentaje_ganancia_tecnico', sa.Float(), nullable=True),
    sa.Column('porcentaje_ganancia_empresa', sa.Float(), nullable=True),
    sa.Column('check_list_pago', sa.String(length=15), nullable=True),
    sa.Column('fecha_salida', sa.Date(), nullable=True),
    sa.Column('reporte', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['nombre_chofer_propietario'], ['usuario.id'], ),
    sa.ForeignKeyConstraint(['tecnico_id'], ['usuario.id'], ),
    sa.ForeignKeyConstraint(['vehiculo_id'], ['vehiculo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reparacion')
    op.drop_table('vehiculo')
    op.drop_table('usuario')
    # ### end Alembic commands ###
