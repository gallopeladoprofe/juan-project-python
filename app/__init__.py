from flask import Flask

app = Flask(__name__)
app.secret_key = b'123'

# referenciales
from app.rutas.referencial.modulo_1.ciudad.ciudad_rutas import ciumod
from app.rutas.referencial.modulo_1.proveedor.proveedor_rutas import proveedormod

modulo0 = '/referencial'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(proveedormod, url_prefix=f'{modulo0}/proveedor')