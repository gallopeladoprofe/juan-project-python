from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash

proveedormod = Blueprint('proveedormod', __name__, template_folder='templates')

@proveedormod.route('/index-proveedor')
def index_proveedor():
    return render_template('index-proveedor.html')

@proveedormod.route('/agregar-proveedor')
def agregar_proveedor():
    return render_template('agregar-proveedor.html')
"""
@proveedormod.route('/save-proveedor', methods=['POST'])
def save_proveedor():
    pass """