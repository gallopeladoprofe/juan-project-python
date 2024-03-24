from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.dao.referencial.estado.EstadoDao import EstadoDao
from app.dao.referencial.funcionario.FuncionarioDao import FuncionarioDao

rscmod = Blueprint('rscmod', __name__, template_folder='templates')

@rscmod.route('/index-registrar-solicitud-compras')
def index_registrar_solicitud_compras():
    pass

@rscmod.route('/formulario-registrar-solicitud-compras')
def formulario_registrar_solicitud_compras():
    estado = EstadoDao()
    funci = FuncionarioDao()
    return render_template('formulario-registrar-solicitud-de-compras.html', \
            estados = estado.getEstados()\
            , lista_funcionarios = funci.getFuncionarios())

# REST
@rscmod.route('/v1/get-funcionario-by-id/<id>')
def get_funcionario_by_id(id):
    funci = FuncionarioDao()
    return funci.getFuncionarioById(id), 200