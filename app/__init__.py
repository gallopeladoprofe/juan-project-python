from flask import Flask

app = Flask(__name__)
app.secret_key = b'123'

# referenciales
from app.rutas.referencial.modulo_1.ciudad.ciudad_rutas import ciumod

# gestionar compras
from app.rutas.gestionar_compras.registrar_solicitud_de_compras.registrar_solicitud_compras_rutas import rscmod

modulo0 = '/referencial'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')

modulo1 = '/gestionar-compras'
app.register_blueprint(rscmod, url_prefix=f'{modulo1}/registrar-solicitud-compras')