from flask import current_app as app
from app.conexion.Conexion import Conexion

class InsumoDao:
	def getInsumos(self):

		querySQL = """
		   SELECT
				i.id,
				i.descripcion,
				i.costo,
				i.referencia_interna,
				i.codigo_de_barras,
				i.stock_minimo,
				i.stock_maximo,
				i.fecha_vecimiento,
				i.id_tipo_insumo, ti.descripcion AS tipo_insumo,
				i.id_unidad_medida, um.descripcion AS unidad_medida,
				i.id_impuesto, imp.descripcion AS impuesto,
				i.id_categoria, cat.descripcion AS categoria,
				i.id_marca, m.descripcion AS marca,
				i.id_estado, e.descripcion AS estado
			FROM
				insumos i
			LEFT JOIN tipo_insumo ti ON ti.id = i.id_tipo_insumo
			LEFT JOIN unidad_medida um ON um.id = i.id_unidad_medida
			LEFT JOIN impuestos imp ON imp.id = i.id_impuesto
			LEFT JOIN categorias cat ON cat.id = i.id_categoria
			LEFT JOIN marcas m ON m.id = i.id_marca
			LEFT JOIN estados e ON e.id = i.id_estado
		"""
		conexion = Conexion()
		con = conexion.getConexion()
		cur = con.cursor()
		try:
			cur.execute(querySQL)
			lista = cur.fetchall()
			return [
				{
					'id': item[0],
					'descripcion': item[1]
					, 'costo' : item[2]
					, 'referencia_interna' : item[3]
					, 'codigo_de_barras': item[4]
					, 'stock_minimo': item[5]
					, 'stock_maximo': item[6]
					, 'fecha_vecimiento': item[7]
					, 'id_tipo_insumo': item[8], 'tipo_insumo': item[9]
					, 'id_unidad_medida': item[10], 'unidad_medida': item[11]
					, 'id_impuesto': item[12], 'impuesto': item[13]
					, 'id_categoria': item[14], 'categoria': item[15]
					, 'id_marca': item[16], 'marca': item[17]
					, 'id_estado': item[18], 'estado': item[19]
				} for item in lista ] if lista else []
		except con.Error as e:
			app.logger.info(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")

		finally:
			cur.close()
			con.close()