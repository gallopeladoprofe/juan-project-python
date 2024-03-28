from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, current_app as app
from app.dao.referencial.estado.EstadoDao import EstadoDao
from app.dao.referencial.funcionario.FuncionarioDao import FuncionarioDao
from app.dao.referencial.prioridad.PrioridadDao import PrioridadDao
from app.dao.referencial.insumo.InsumoDao import InsumoDao
from app.dao.gestionar_compras.registrar_solicitud_compras.SolicitudComprasDao \
    import SolicitudComprasDao, SolicitudCompradto, SolicitudCompraDetalledto

rscmod = Blueprint('rscmod', __name__, template_folder='templates')

@rscmod.route('/index-registrar-solicitud-compras')
def index_registrar_solicitud_compras():
    pass

@rscmod.route('/formulario-registrar-solicitud-compras')
def formulario_registrar_solicitud_compras():
    estado = EstadoDao()
    funci = FuncionarioDao()
    priori = PrioridadDao()
    insumo = InsumoDao()
    return render_template('formulario-registrar-solicitud-de-compras.html', \
            estados = estado.getEstados()\
            , lista_funcionarios = funci.getFuncionarios()\
            , lista_prioridades = priori.getPrioridades()\
            , lista_insumos = insumo.getInsumos())

# REST
@rscmod.route('/v1/get-funcionario-by-id/<id>')
def get_funcionario_by_id(id):
    funci = FuncionarioDao()
    return funci.getFuncionarioById(id), 200

# REST
@rscmod.route('/v1/registrar-solicitud-compra', methods=['POST'])
def registrar_solicitud_compra():

    # Recuperar información
    id_estado = request.json.get('id_estado')
    id_funcionario = request.json.get('id_funcionario')
    id_prioridad = request.json.get('id_prioridad')
    fecha_entrega = request.json.get('fecha_entrega')
    detalle_insumo = request.json.get('detalle_insumo')

    # Validar
    if not id_estado or not id_funcionario or not id_prioridad\
        or not fecha_entrega or not detalle_insumo or len(detalle_insumo)==0:
        app.logger.error({ 'success': None, 'error': 'Hay errores en el payload de POST' })
        return { 'success': None, 'error': 'Hay errores en el payload de POST, consulte al administrador' },400

    detalle_insumo_dto = [ SolicitudCompraDetalledto(None, item['id_insumo'], item['cantidad']) for item in detalle_insumo ]

    dto = SolicitudCompradto(None, None, id_estado, id_funcionario, id_prioridad, 1, fecha_entrega, detalle_insumo_dto)

    solicitud_dao = SolicitudComprasDao()
    isSaved = solicitud_dao.insertSolicitud(dto)

    if isSaved:
        return { 'success': 'Inserción exitosa', 'error': None },200
    else:
        return { 'success': None, 'error': 'No se pudo registrar la solicitud de compras, consulte al administrador' },500